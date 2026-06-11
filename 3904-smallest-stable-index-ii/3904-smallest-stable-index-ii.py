class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)
        prefixes = [nums[0]]

        for i in range(1, n):
            prefixes.append(max(nums[i],prefixes[i-1]))

        suffixes = [0] * n
        suffixes[-1] = nums[-1]

        for i in range(n-2,-1,-1):
            suffixes[i] = min(nums[i],suffixes[i+1])

        for i in range(n):
            if prefixes[i] - suffixes[i] <= k:
                return i
        
        return -1