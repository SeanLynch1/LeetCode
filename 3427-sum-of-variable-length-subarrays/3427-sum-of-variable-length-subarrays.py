class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        
        # [0,4,1,2,4] #
        # [0,0,4,5,7,11]

        # 0 - 0 = 0 -> 0
        # 1 - 4 = 0 -> 0
        # 2 - 1 = 1 -> 2
        # 3 - 2 = 2 -> 3
        # 4 - 4 = 0 -> 4

        prefixes = [0]
        ans = 0

        for n in nums:
            prefixes.append(n + prefixes[-1])

        for i in range(len(nums)):
            right = i
            left = max(0, i - nums[i])
            ans += prefixes[right + 1] - prefixes[left]

        return ans