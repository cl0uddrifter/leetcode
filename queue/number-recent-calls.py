# Problem 933
# Run   O(n)
# Space O(n)

class RecentCounter:

    def __init__(self):
        self.reqs = []

    def ping(self, t: int) -> int:
        self.reqs.insert(0, t)
        rng = t - 3000
        while self.reqs[-1] < rng:
            self.reqs.pop()
        return len(self.reqs)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
