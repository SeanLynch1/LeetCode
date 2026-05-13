from collections import defaultdict, deque
from math import sqrt

class Solution:
    def largestComponentSize(self, nums):
        # Map: prime factor -> list of numbers
        factor_map = defaultdict(list)

        def get_factors(x):
            factors = set()
            d = 2
            while d * d <= x:
                if x % d == 0:
                    factors.add(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                factors.add(x)
            return factors

        # Build factor graph
        num_to_factors = {}
        for num in nums:
            f = get_factors(num)
            num_to_factors[num] = f
            for fac in f:
                factor_map[fac].append(num)

        visited = set()

        def bfs(start):
            q = deque([start])
            visited.add(start)
            size = 0

            while q:
                node = q.popleft()
                size += 1

                for fac in num_to_factors[node]:
                    for nei in factor_map[fac]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

                    # optional optimization: clear to avoid re-processing
                    factor_map[fac] = []

            return size

        best = 0
        for num in nums:
            if num not in visited:
                best = max(best, bfs(num))

        return best