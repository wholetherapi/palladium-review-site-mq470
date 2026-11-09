import argparse
import csv
from collections import defaultdict

from src.drift import DriftEstimator

def load(path):
    series = defaultdict(list)
    with open(path, newline="") as handle:
        for row in csv.DictReader(handle):
            series[row["pool"]].append(float(row["clock_offset_ms"]))
    return series

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace", required=True)
    args = parser.parse_args()
    series = load(args.trace)
    for pool, offsets in sorted(series.items()):
        estimator = DriftEstimator()
        for value in offsets:
            estimator.update(value)
        print(f"{pool}: final drift estimate {estimator.state:.2f} ms")

if __name__ == "__main__":
    main()
