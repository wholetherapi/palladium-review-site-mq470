# Hedgerow

Streaming parser toolkit for semi-structured logs (WPS '26).

Hedgerow reads line-delimited input once, applies a per-line schema, and emits
typed events. It is intended for log pipelines where the schema varies by
message class.

## Layout

- `src/tokenizer.py` — zero-copy tokenizer
- `src/parser.py` — schema dispatch and event construction
- `data/sample_logs.ndjson` — sample corpus used in the evaluation
- `experiments/bench_e2e.py` — end-to-end throughput harness
