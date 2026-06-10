class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #[2,2,2,7]

        # 2: 0010
        # 2: 0010
        # 2: 0010
        # 7: 0111

        # count of 1s at idx 0: 1
        # count of 1s at idx 1: 4
        # count of 1s at idx 2: 1
        # count of 1s at idx 3: 0

        # if 3 goes into the count, you have a triplet, the remainder will only every be 1, that 1 represents the value at that index of the unique number

        res = 0
        # 0000

        bits = 32
        # 0000 0000 0000 0000 0000 0000 0000 0000

        # 0 - 31
        for i in range(bits):

            count = 0

            #compare by index
            for n in nums:
                if n & (1 << i):
                    count += 1

            if count % 3:
                # 0000
                # 0010
                res = res | (1 << i)

            if res >= 2**31:
                res -= 2**32

        return res