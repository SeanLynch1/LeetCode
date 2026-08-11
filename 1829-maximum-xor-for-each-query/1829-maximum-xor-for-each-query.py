class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        target = (2 ** maximumBit) - 1
        prefixes = [0]
        output = []

        for i in range(len(nums)):
            prefixes.append(prefixes[-1] ^ nums[i])

        for i in range(len(prefixes)-1,0,-1):
            output.append(prefixes[i] ^ target)

        return output

