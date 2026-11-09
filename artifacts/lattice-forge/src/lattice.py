import itertools
import math

def phi_p(design, p=15):
    total = 0.0
    for first, second in itertools.combinations(design, 2):
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(first, second)))
        total += dist ** (-p)
    return total ** (1.0 / p)

def maximin_score(design):
    best = float("inf")
    for first, second in itertools.combinations(design, 2):
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(first, second)))
        best = min(best, dist)
    return best

def build_design(runs, factors, shift=0.37):
    design = []
    for i in range(runs):
        row = [((i * (k + 1) + shift * i) % runs) / float(runs) for k in range(factors)]
        design.append(row)
    return design

def projection_balance(design, runs):
    columns = list(zip(*design))
    return [max(c.count(level) for level in sorted(set(c))) for c in columns]
