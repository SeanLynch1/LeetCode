class Solution:
    def numberOfWays(self, s: str) -> int:
        
        #  0 0 1 1 1 0 1 1 0 1   

        # zeroes
        # [1,2,2,2,2,3,3,3,4,4]

        # ones
        # [0,0,1,2,3,3,4,5,5,6]

        count = 0
        zeroes = [0]
        ones = [0] 

        for num in s:

            if num == "0":
                zeroes.append(zeroes[-1] + 1)
                ones.append(ones[-1])
            else:
                zeroes.append(zeroes[-1])
                ones.append(ones[-1] + 1)
        
        for idx, num in enumerate(s):

            if num == "0":
                left = ones[idx]
                if left > 0:
                    right = ones[-1] - left
                    count += left * right
            else:
                left = zeroes[idx]
                if left > 0:
                    right = zeroes[-1] - left
                    count += left * right

        return count