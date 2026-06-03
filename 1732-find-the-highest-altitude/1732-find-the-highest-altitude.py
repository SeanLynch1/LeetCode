class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        total = 0
        ans = 0

        for val in gain:

            total += val
            ans = max(ans, total)

        return ans