import pandas as pd

def clean(input_file):
    df = pd.read_csv(input_file)
    return df


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='combined data file (CSV)')
    parser.add_argument('output_file', help='cleaned data file (CSV)')
    args = parser.parse_args()
    clean = clean(args.input_file)
    clean.to_csv(args.output_file, index=False)