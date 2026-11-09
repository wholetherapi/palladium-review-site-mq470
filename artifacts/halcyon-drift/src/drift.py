import math

class DriftEstimator:
    def __init__(self, alpha=0.2):
        self.alpha = alpha
        self.state = None

    def update(self, offset_ms):
        if self.state is None:
            self.state = float(offset_ms)
        else:
            self.state = self.alpha * float(offset_ms) + (1 - self.alpha) * self.state
        return self.state

    def skew(self, logical_seconds):
        return self.state * logical_seconds / 1000.0

class CorrectionController:
    def __init__(self, threshold_ms=5.0, step_ms=1.0):
        self.threshold_ms = threshold_ms
        self.step_ms = step_ms

    def correction(self, estimate_ms):
        if abs(estimate_ms) < self.threshold_ms:
            return 0
        direction = -1.0 if estimate_ms > 0 else 1.0
        ticks = math.floor(abs(estimate_ms) / self.step_ms)
        return direction * ticks * self.step_ms
