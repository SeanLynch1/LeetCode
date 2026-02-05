class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        medians = []
        output = 0

        def gcd(a:int, b:int):
            
            if b == 0:
                return a
            
            return gcd(b, a%b)

        cycles = gcd(len(arr), k)

        for c in range(cycles):
            jump = (c + k) % n
            temp = [arr[c % n]]

            while jump != c:
                temp.append(arr[jump])

                jump += k
                jump %= n

            temp.sort()
            median_temp = temp[int(len(temp) / 2)]
            medians.append(median_temp)
        
        for c in range(cycles):
            jump = (c + k) % n
            output += abs(medians[c] - arr[c % n])

            while jump != c:
                output += abs(medians[c] - arr[jump])

                jump += k
                jump %= n
            
        return output