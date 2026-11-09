class Stage:
    def __init__(self, name, predict):
        self.name = name
        self.predict = predict

class Cascade:
    def __init__(self, gate, small, large):
        self.gate = gate
        self.small = small
        self.large = large

    def run(self, inputs, features):
        outputs = []
        for item, feat in zip(inputs, features):
            if self.gate.escalated(feat):
                outputs.append((self.large.name, self.large.predict(item)))
            else:
                outputs.append((self.small.name, self.small.predict(item)))
        return outputs

    def escalation_rate(self, features):
        if not features:
            return 0.0
        return sum(1 for f in features if self.gate.escalated(f)) / float(len(features))
