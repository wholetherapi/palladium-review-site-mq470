import argparse
import time

from src.parser import parse_stream

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--repeats", type=int, default=200)
    args = parser.parse_args()
    lines = open(args.corpus).read().splitlines()
    started = time.perf_counter()
    events = 0
    for _ in range(args.repeats):
        events += sum(1 for _ in parse_stream(lines))
    elapsed = time.perf_counter() - started
    print("events=%d seconds=%.3f rate=%.0f/s" % (events, elapsed, events / elapsed))

if __name__ == "__main__":
    main()
