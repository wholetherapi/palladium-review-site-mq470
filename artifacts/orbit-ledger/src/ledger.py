import hashlib
import json
from datetime import datetime, timezone

def digest(payload):
    encoded = json.dumps(payload, sort_keys=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()

class Ledger:
    def __init__(self):
        self.entries = []
        self.head = "0" * 64

    def append(self, kind, payload):
        entry = {
            "kind": kind,
            "payload": payload,
            "prev": self.head,
            "recorded_at": datetime.now(timezone.utc).isoformat(),
        }
        entry["hash"] = digest(entry)
        self.head = entry["hash"]
        self.entries.append(entry)
        return entry

    def to_json(self):
        return json.dumps({"head": self.head, "entries": self.entries}, indent=2)
