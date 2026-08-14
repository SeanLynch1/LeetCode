class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        # [1, 2, 4, 3, 5, 1]

        # [1, 2, 4]

        output = 0
        for i in range(len(nums)):
            
            lowest = nums[i]
            highest = nums[i]
            for j in range(i, len(nums)):
                nxt = nums[j]

                lowest = min(lowest, nxt)
                highest = max(highest, nxt)
                output += highest - lowest

        return output