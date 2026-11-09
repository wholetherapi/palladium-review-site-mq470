from collections import defaultdict

class PoolAllocator:
    def __init__(self, pools):
        self.pools = list(pools)
        self.assigned = defaultdict(int)

    def allocate(self, job_id, demand, scores):
        ranked = sorted(self.pools, key=lambda p: scores.get(p, 0.0), reverse=True)
        for pool in ranked:
            if self.assigned[pool] + demand <= self.pools[pool]:
                self.assigned[pool] += demand
                return pool
        raise RuntimeError(f"no pool with capacity for job {job_id}")

    def release(self, pool, amount):
        self.assigned[pool] = max(0, self.assigned[pool] - amount)

    def utilization(self):
        return {
            pool: self.assigned[pool] / float(self.pools[pool])
            for pool in self.pools
        }
