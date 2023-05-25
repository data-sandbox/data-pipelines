import argparse
import json


def get_statistics(log, output):
    """
    Compute temperature statistics from log file.
    """
    with open('temperature.log', 'r') as f:
        array = [line.rstrip() for line in f]

    stats = {'min': min(array),
             'max': max(array)}

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
