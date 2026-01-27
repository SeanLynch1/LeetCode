class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixes = [1]
        for i in range(1, len(nums)):
            prev_nums = nums[i - 1]
            prefixes.append(prev_nums * prefixes[-1])

        for j in range(len(prefixes)-1,0,-1):
            prefixes[j - 1] *= nums[j]
            nums[j - 1] *= nums[j]

        return prefixes