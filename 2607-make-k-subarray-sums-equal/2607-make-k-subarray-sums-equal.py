from typing import List
import math

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        cycles = math.gcd(n, k)
        output = 0

        for c in range(cycles):
            temp = []
            j = c
            while True:
                temp.append(arr[j])
                j = (j + k) % n
                if j == c:
                    break

            temp.sort()
            median = temp[len(temp) // 2]
            output += sum(abs(x - median) for x in temp)

        return output
