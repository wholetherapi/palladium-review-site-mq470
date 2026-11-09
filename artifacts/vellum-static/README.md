# Vellum Static

Request-time template renderer (internal experiment).

Vellum Static resolves templates without a build step, caching compiled
fragments per request class.

## Layout

- `src/renderer.py` — fragment cache and substitution engine
- `data/site_fixture.json` — fixture site used in the draft experiments
- `experiments/render_sample.py` — render timing harness
