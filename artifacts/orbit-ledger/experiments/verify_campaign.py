import argparse

from src.verify import load, verify

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    args = parser.parse_args()
    ok, message = verify(load(args.manifest))
    print("verified" if ok else "failed", message)

if __name__ == "__main__":
    main()
