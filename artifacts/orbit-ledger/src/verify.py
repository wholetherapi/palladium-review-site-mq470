import json

from src.ledger import digest

def verify(manifest):
    head = "0" * 64
    for entry in manifest["entries"]:
        if entry["prev"] != head:
            return False, "broken chain at %s" % entry.get("kind")
        body = dict(entry)
        stored = body.pop("hash")
        if digest(body) != stored:
            return False, "hash mismatch at %s" % entry.get("kind")
        head = stored
    if manifest["head"] != head:
        return False, "head mismatch"
    return True, "ok"

def load(path):
    with open(path) as handle:
        return json.load(handle)
