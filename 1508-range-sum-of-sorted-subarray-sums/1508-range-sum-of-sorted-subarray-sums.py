class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        # [1,2,3,4]
        # [0,1,3,6,10]

        MOD = (10 ** 9) + 7
        output = []
        for i in range(len(nums)):
            start = 0
            for j in range(i, len(nums)):
                start += nums[j]
                output.append(start)

        output.sort()

        res = 0
        for i in range(left-1,right):
            res += (output[i])

        return res % MOD