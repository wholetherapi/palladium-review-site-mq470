from collections import namedtuple

from src.tokenizer import tokenize, classify

Event = namedtuple("Event", "kind fields")

SCHEMAS = {
    "request": ("ts", "service", "status", "latency"),
    "job": ("ts", "queue", "state", "attempt"),
}

def parse_line(line):
    kind = None
    fields = {}
    for token in tokenize(line):
        tag = classify(token)
        if tag == "tag" and token.strip("[]").lower() in SCHEMAS:
            kind = token.strip("[]").lower()
        elif tag == "word" and "=" in token:
            key, value = token.split("=", 1)
            fields[key] = value
    if kind is None:
        return None
    wanted = SCHEMAS[kind]
    ordered = tuple(fields.get(name) for name in wanted)
    return Event(kind, ordered)

def parse_stream(lines):
    for line in lines:
        event = parse_line(line)
        if event is not None:
            yield event
