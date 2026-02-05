class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        output = 0

        def gcd(a:int, b:int):
            
            if b == 0:
                return a
            
            return gcd(b, a%b)

        cycles = gcd(len(arr), k)

        for c in range(cycles):
            jump = (c + k) % n
            temp = [arr[c]]

            while jump != c:
                temp.append(arr[jump])

                jump += k
                jump %= n

            temp.sort()
            median = temp[int(len(temp) / 2)]
            
            for j in range(len(temp)):
                output += abs(median - temp[j])

        return output