class Solution:
    def subsets(self, nums):
        res = [[]]

        for num in nums:
            # for each existing subset, add a new one with num
            res += [curr + [num] for curr in res]

        return res