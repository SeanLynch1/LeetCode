class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        ops = 0
        
        
        while True:

            positives = [num for num in nums if num > 0]
            if not positives:
                return ops

            lowest = min(positives)

            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] -= lowest

            positives = [num for num in nums if num > 0]

            ops += 1