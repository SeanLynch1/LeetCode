class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        target = (1 << maximumBit) - 1
        xor = 0
        output = []

        for i in range(len(nums)):
            xor ^= nums[i]

        for i in range(len(nums)-1,-1,-1):
            output.append(xor ^ target)
            xor ^= nums[i]

        return output