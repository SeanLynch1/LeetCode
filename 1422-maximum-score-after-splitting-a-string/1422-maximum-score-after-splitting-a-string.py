class Solution:
    def maxScore(self, s: str) -> int:
        
        # zers = [0, 1, 1, 1, 1, 2, 2]

        # ones = [0, 0, 1, 2, 3, 3, 4]
        ans = 0
        zeroes = [0]
        ones = [0]


        for letter in s:
            zeros_count = zeroes[-1] 
            ones_count = ones[-1] 

            if letter == "0":
                zeros_count += 1
            else:
                ones_count += 1

            zeroes.append(zeros_count)
            ones.append(ones_count)

        print(f"zers: {zeroes}")
        print(f"ones: {ones}")
        n = len(s)
        for i in range(1, n):
            
            ones_count = ones[n] - ones[i]
            zero_count = zeroes[i]
            print(f"i = {i}")
            print(f"zero_count = {zero_count}")
            print(f"ones_count = {ones_count}")
            ans = max(ans, zero_count + ones_count)

        return ans


