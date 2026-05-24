class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        mapping = Counter(nums)
        if len(nums) == 1:
            if nums[0] == 0:
                return 0
            else:
                return 1
        else:
            if 0 in mapping:
                return len(mapping) - 1
            else:
                return len(mapping)