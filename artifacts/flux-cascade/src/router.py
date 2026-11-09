import json

class CascadeGate:
    def __init__(self, weights, bias, threshold=0.5):
        self.weights = list(weights)
        self.bias = float(bias)
        self.threshold = float(threshold)

    def score(self, features):
        total = self.bias
        for w, x in zip(self.weights, features):
            total += w * x
        return 1.0 / (1.0 + pow(2.718281828, -total))

    def escalated(self, features):
        return self.score(features) >= self.threshold

def load_gate(path):
    with open(path) as handle:
        payload = json.load(handle)
    return CascadeGate(payload["weights"], payload["bias"], payload["threshold"])
