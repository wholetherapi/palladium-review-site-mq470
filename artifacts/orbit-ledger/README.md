# Orbit Ledger

Provenance recording for simulation campaigns (CRI '27).

Orbit Ledger writes a hash-chained manifest for every campaign: inputs,
environment digests and derived artifacts. A companion verifier replays the
manifest to confirm that the campaign can be rebuilt.

## Layout

- `src/ledger.py` — append-only hash-chained ledger
- `src/verify.py` — manifest verification utilities
- `data/campaign_manifest.json` — small example campaign
- `experiments/verify_campaign.py` — verification driver
