import argparse
import json

from src.router import load_gate, CascadeGate
from src.cascade import Cascade, Stage

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--calibration", required=True)
    parser.add_argument("--prompts", type=int, default=1000)
    args = parser.parse_args()

    gate = load_gate(args.calibration)
    cascade = Cascade(
        gate=gate,
        small=Stage("small", lambda x: x["small_answer"]),
        large=Stage("large", lambda x: x["large_answer"]),
    )
    features = [[0.4, 0.1, 0.9, 0.2] for _ in range(args.prompts)]
    print("escalation_rate=%.3f" % cascade.escalation_rate(features))

if __name__ == "__main__":
    main()
