import argparse
import pandas as pd
import json


def get_statistics(log, output):
    """
    Compute temperature statistics from log file.
    """
    df = pd.read_csv(str(log), names=['date', 'temperature(F)'])

    stats = {'current': df['temperature(F)'].iloc[-1],
             'avg': df.loc[:, 'temperature(F)'].mean(),
             'min': df.loc[:, 'temperature(F)'].min(),
             'max': df.loc[:, 'temperature(F)'].max()}

    with open(str(output), 'w') as f:
        json.dump(stats, f)

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--log', help="Name of log file.")
    parser.add_argument(
        '--output', help="Name of output file.")
    args = parser.parse_args()

    get_statistics(args.log, args.output)
