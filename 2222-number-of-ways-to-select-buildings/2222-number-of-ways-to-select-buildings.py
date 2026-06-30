class Solution:
    def numberOfWays(self, s: str) -> int:
        
        #  0 0 1 1 1 0 1 1 0 1   

        # zeroes
        # [1,2,2,2,2,3,3,3,4,4]

        # ones
        # [0,0,1,2,3,3,4,5,5,6]

        count = 0
        left_0 = left_1 = 0
        right_1 = s.count('1')
        right_0 = s.count('0')

        for idx, num in enumerate(s):
            if num == "0":
                right_0 -=1
                count += left_1 * right_1
                left_0 += 1
            else:
                right_1 -=1
                count += left_0 * right_0
                left_1 += 1

        return count