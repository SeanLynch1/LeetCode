from typing import List
import math

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        g = math.gcd(n, k)
        ans = 0

        for start in range(g):
            cycle = []
            j = start
            while True:
                cycle.append(arr[j])
                j = (j + k) % n
                if j == start:
                    break

            cycle.sort()
            med = cycle[len(cycle) // 2]
            ans += sum(abs(x - med) for x in cycle)

        return ans
