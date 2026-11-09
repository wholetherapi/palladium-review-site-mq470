# Flux Cascade

Code release for *Cascade Routing for Adaptive Computation* (ICAC '27).

The router learns a per-example gate that decides whether an input can be
answered by the compact first stage or must be escalated to the large stage.

## Layout

- `src/router.py` — gate model and threshold calibration
- `src/cascade.py` — two-stage inference pipeline
- `data/calibration.json` — gate calibration split summary
- `experiments/benchmark.py` — throughput/accuracy sweep used in the paper
