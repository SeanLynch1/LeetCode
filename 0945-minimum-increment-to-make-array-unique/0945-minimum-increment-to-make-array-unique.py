class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        moves = 0

        nums.sort()
        print(nums)

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                prev = nums[i]
                nums[i] = nums[i - 1] + 1
                moves += (nums[i] - prev)

        print(nums)
        return moves