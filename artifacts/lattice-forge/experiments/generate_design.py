import argparse

from src.lattice import build_design, phi_p, maximin_score

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=16)
    parser.add_argument("--factors", type=int, default=4)
    args = parser.parse_args()
    design = build_design(args.runs, args.factors)
    print("phi_p=%.4f maximin=%.4f" % (phi_p(design), maximin_score(design)))
    for row in design:
        print(",".join("%.3f" % value for value in row))

if __name__ == "__main__":
    main()
