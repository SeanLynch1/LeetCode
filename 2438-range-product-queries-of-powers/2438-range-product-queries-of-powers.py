class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        # 0011 0011 51
        # 0000 0001 1
        # 0000 0010 2
        # 0000 0100 0

        # 0010 0000 32
        # 0001 0000 16
        # 0000 0010 2
        # 0000 0001 1
        
        res = []
        prefix = [1]
        curr = 1
        power = 0

        while n > 0:
            binary = f"{n:08b}"
            print(f"{binary[:4]} {binary[4:]}")

            bit = n & 1   # get rightmost bit
            
            if bit == 1:
                curr *= 2 ** power
                prefix.append(curr)

            power += 1
            n >>= 1       # shift right
        
        print(prefix)
        for l, r in queries:
            
            res.append(int(prefix[r + 1] / prefix[l]) % (10 ** 9 + 7))

        # 1, 2, 4, 8,  16,   32
        # 1, 2, 8, 64, 1024, 32768
        return res