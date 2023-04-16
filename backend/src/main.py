import sys, os
import pickle

from flask import Flask
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS, cross_origin
sys.path.append(os.path.join(sys.path[0],'assessment'))
from model_creation import create_model

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class Assessment(Resource): 
    @cross_origin()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('alphaBeta')
        parser.add_argument('at8')
        parser.add_argument('at8Ffp')
        parser.add_argument('gfap')
        parser.add_argument('tau')
        parser.add_argument('tau2')
        parser.add_argument('tdp')
        args = parser.parse_args()
        with (open(os.path.join(sys.path[0],'assessment', 'final_model.pkl'), "rb")) as f:
            model = pickle.load(f)
            prediction = model.predict([[args['gfap'], args['at8'], args['at8Ffp'], args['alphaBeta'], args['tau2'], args['tdp'], args['tau']]])
            dementia_analysis = "at_risk" if prediction[0] == 1 else "not_at_risk"
            return dementia_analysis, 201

final_model = create_model()
with open(os.path.join(sys.path[0],'assessment', 'final_model.pkl'), 'wb+') as out:
    pickle.dump(final_model, out)

api.add_resource(Assessment, '/assessment')

if __name__ == '__main__':
    app.run(debug=True)