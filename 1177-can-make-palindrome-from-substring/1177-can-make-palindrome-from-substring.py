class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # a c a b b a
        # 0 1 2 2 3 3 3

        # a : 0000 0001
        # b : 0000 0010
        # c : 0000 0100

        #  : 0000 0000 = 0
        # a: 0000 0001 = 1
        # c: 0000 0101 = 5
        # a: 0000 0100 = 4
        # b: 0000 0110 = 6
        # b: 0000 0100 = 4 
        # a: 0000 0101 = 5

        res = []
        xor_prefix = [0]
        c = 'a'

        for letter in s:
            val = ord(letter) - ord(c)
            xor_prefix.append(xor_prefix[-1] ^ (1 << val))

        for left, right, replacements in queries:
            xor_val = xor_prefix[right + 1] ^ xor_prefix[left]

            count = 0
            while xor_val > 0:
                count += 1 & xor_val
                xor_val >>= 1

            if replacements >= count // 2:
                res.append(True)
            else:
                res.append(False)

        return res