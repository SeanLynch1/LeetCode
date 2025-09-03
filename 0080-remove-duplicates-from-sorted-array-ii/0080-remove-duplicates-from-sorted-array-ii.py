class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if two before me does not equal me, change me

        write = 2

        for read in range(2, len(nums), 1):

            if nums[read] == nums[write - 2]:
                continue
            else:
                nums[write] = nums[read]
                write += 1

        return write