class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # 2, 5
        # [1, 0, -1, 2, -3,  5, 2, 1, -5]
        # [1, 1,  0, 2, -1,  4, 6, 7,  2]

        ans = float('inf')
        prefixes = []

        last = 0
        for n in nums:
            prefixes.append(last+n)
            last += n

        start = 0
        for i in range(len(prefixes) - (l - 1)):
        
            for j in range(i, min(i + r, len(prefixes))):
                total = prefixes[j] - start
                if j - i >= (l - 1) and total > 0:
                    ans = min(ans, total)
            
            start = prefixes[i]

        return ans if ans != float('inf') else -1