class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # [3,4,3,5,6,5,1,6,4]
        # [0000] start with 0
        # [0011] add 3 -> [0011] -> becomes 3
        # [0100] add 4 -> [0111] -> becomes 7
        # [0011] add 3 -> [0100] -> becomes 4
        # [0101] add 5 -> [0001] -> becomes 1
        # [0110] add 6 -> [0111] -> becomes 7
        # [0101] add 5 -> [0010] -> becomes 2
        # [0001] add 1 -> [0011] -> becomes 3
        # [0110] add 6 -> [0101] -> becomes 5
        # [0100] add 4 -> [0001] -> becomes 1
        # 0000 0000 0000 0000 0000 0000 0000 0000 -> 32 bit, represents ints

        res = 0

        for n in nums:
            res = res ^ n

        return res