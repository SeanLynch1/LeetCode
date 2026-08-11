class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        # 0010
        # 0011
        #
        # 0001 -> add 1
        # 0100
        #
        # 0101 -> add 5
        # 0111
        #
        # 0010 -> add 2
        # 0101 -> 5 (needed)
        #
        # 0111

        target = (2 ** maximumBit) - 1
        prefixes = []
        output = []

        last = 0
        for i in range(len(nums)):

            prefixes.append(last ^ nums[i])
            last = prefixes[-1]

        print(prefixes)

        for i in range(len(prefixes)-1,-1,-1):
            output.append(prefixes[i] ^ target)

        return output

