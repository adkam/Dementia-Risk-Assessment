import pandas as pd
import sys, os

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold, RepeatedStratifiedKFold, GridSearchCV

def read_file(file, path = os.path.join(sys.path[0],'assessment', 'data'), extra = ''):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR,'assessment', 'data') + '/' + extra
    df = pd.read_csv(path + file)
    return df

def clean_donor_data():
   df = read_file('donor_information.csv')
   df['nincds_arda_diagnosis'] = df['nincds_arda_diagnosis'].replace("Possible Alzheimer'S Disease", "Probable Alzheimer'S Disease")
   df = df[df['nincds_arda_diagnosis'] != 'Dementia, Type Unknown']
   return df

def clean_protein_pathology_quantifications():
   df1 = read_file('protein_and_pathology_quantifications.csv')
   df2 = df1.pivot_table(index = ['donor_id', 'donor_name'],
                      columns = ['structure_acronym'],
                      values = df1.columns[4:].tolist(),
                      aggfunc = 'sum').reset_index()
   df2.columns = ['_'.join(col) if col[0] != 'donor_id' or col[0] != 'donor_name' else col for col in df2.columns]
   df2 = df2.rename({'donor_id_': 'donor_id',
                  'donor_name_': 'donor_name'}, axis = 1)
   return df2

def clean_data():
   df1 = clean_donor_data()
   df2 = clean_protein_pathology_quantifications()
   df3 = read_file('group_weights.csv')
   return df1, df2, df3

def initialize():
  df1, df2, df3 = clean_data()
  merged = df1.merge(df2, on = 'donor_id')
  temp = df3.rename({'Donor ID': 'name'}, axis = 1)
  merged = merged.merge(temp, on = 'name')
  return merged

def missing_imputation(merge, method = 'mean'):
  res = merge.isna().sum()
  res = res[res.values > 0]
  if method == 'drop':
    merge = merge.dropna(subset = ['apo_e4_allele'], axis = 0)
    merge = merge[~merge.isna().any(axis = 1)]
  else:
    merge = merge.dropna(subset = ['apo_e4_allele'], axis = 0)
    merge = merge.fillna(merge.mean())
  return res, merge

def mappings(merge):
  index = ['78', '79', '81', '82', '83', '84', '85', '86', '87',
           '88', '89', '90-94', '95-99', '100+']
  mapping = {}
  for i,j in zip(index, range(1, len(index) + 1)):
    mapping[i] = j
  merge['age'] = merge['age'].map(mapping)
  merge['sex'] = merge['sex'].map({'M': 1, 'F': 0})
  merge['ever_tbi_w_loc'] = merge['ever_tbi_w_loc'].map({'Y': 1, 'N': 0})
  merge['act_demented'] = merge['act_demented'].map({'No Dementia': 0, 'Dementia': 1})
  merge['nincds_arda_diagnosis'] = merge['nincds_arda_diagnosis'].map({'No Dementia': 0, "Probable Alzheimer'S Disease": 1})
  merge['apo_e4_allele'] = merge['apo_e4_allele'].map({'Y': 1, 'N': 0})
  return merge

def create_xy(merge, drop):
  drop = drop + ['donor_id', 'name', 
            'dsm_iv_clinical_diagnosis', 'donor_name', 'hispanic',
            'longest_loc_duration', 'race',
            'act_demented']
  
  merge = merge.drop(drop, axis = 1)
  _, merge = missing_imputation(merge, 'drop')

  y = merge['nincds_arda_diagnosis']
  X = merge.drop(['nincds_arda_diagnosis'], axis = 1)
  return X, y

def selection_r2(merge):
  merge['age_at_first_tbi'] = merge['age_at_first_tbi'].apply(lambda x: 1 if x > 0 else 0)
  merge = merge.rename({'age_at_first_tbi': 'ever_tbi'}, axis = 1)
  merge = merge.drop(['Weight', 'control_set',
                      'il_1b_pg_per_mg_TCx',
                      'bdnf_pg_per_mg_TCx', ], axis = 1)
  return merge

def prepare_for_tree():
  merge = initialize()
  merge = mappings(merge)
  drop = merge.isna().sum()[merge.isna().sum() > 8].index.tolist()
  X, y = create_xy(merge, drop)
  X = selection_r2(X)
  X = X.reset_index(drop = True)
  y = y.reset_index(drop = True)
  return X, y

def final(X, y, cv):
  X = X[['ihc_gfap_ffpe_TCx',
 'ihc_at8_TCx',
 'ihc_at8_ffpe_TCx',
 'ihc_a_beta_ffpe_TCx',
 'ihc_tau2_ffpe_TCx',
 'ihc_ptdp_43_ffpe_TCx',
 'tau_ng_per_mg_TCx']]

  alphas = []
  alpha_cv = StratifiedKFold(n_splits = 10)
  for train_idx, test_idx in alpha_cv.split(X, y):
    X_train, y_train = X.iloc[train_idx, :], y[train_idx]
    X_test, y_test = X.iloc[test_idx, :], y[test_idx]
    selector = DecisionTreeClassifier(random_state = 77)
    alphas += list(selector.cost_complexity_pruning_path(X_train, y_train)['ccp_alphas'])
  alphas = list(set(alphas))

  params = {'ccp_alpha': alphas,
            'max_leaf_nodes': range(3, 15)}
  clf = DecisionTreeClassifier(random_state = 77)
  grid = GridSearchCV(clf, params, scoring = 'accuracy', cv = cv)
  grid.fit(X, y)

  return grid, alphas


def create_model():
    X, y = prepare_for_tree()
    cv = RepeatedStratifiedKFold(n_splits = 10, n_repeats = 5, random_state = 315)
    model, alphas = final(X, y, cv)
    return model.best_estimator_