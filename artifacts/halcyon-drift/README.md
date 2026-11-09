# Halcyon Drift

Reference implementation for *Halcyon Drift: Drift-Aware Scheduling for Shared
Accelerator Pools* (SLS '27).

## Layout

- `src/drift.py` — exponential drift estimator and correction controller
- `src/allocator.py` — pool allocator used by the scheduler
- `data/pool_trace.csv` — telemetry collected during the paper evaluation
- `experiments/run_eval.py` — reproduces the latency summary in Table 3

## Usage

```
python experiments/run_eval.py --trace data/pool_trace.csv
```
