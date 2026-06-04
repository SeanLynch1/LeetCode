class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        prefixes = [0]
        ans = [0] * len(nums)

        for num in nums:
            prefixes.append(prefixes[-1] + num)

        print(prefixes)
        suffix = 0
        for i in range(len(nums)-1,-1,-1):
            ans[i] = abs(prefixes[i] - suffix)
            suffix += nums[i]

        return ans
