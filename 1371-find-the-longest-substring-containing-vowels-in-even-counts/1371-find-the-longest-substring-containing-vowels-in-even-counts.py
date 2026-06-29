class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        max_len = 0
        
        #1132211

        # 0001 1
        # 0001 and 1
        # 0000 makes 0
        # 0011 3
        # 0010 and 2
        # 0001 makes 1
        # 0010 and 2
        # 0011 makes 3
        # 0001 and 1
        # 0010 makes 2
        # 0001 and 1
        # 0011 makes 3

        mapping = {0: 0}
        vowels = {'a':1,'i':2,'e':3,'o':4,'u':5}

        n = len(s)
        xors = [0] * (n + 1)

        for i in range(n):
            
            letter = s[i]
            val = xors[i]

            if letter in vowels:
                val ^= 1 << vowels[letter]
                xors[i + 1] = val

                if val not in mapping:
                    mapping[val] = i + 1
            else:
                xors[i + 1] = xors[i]

            if val in mapping:
                max_len = max(max_len, i - mapping[val] + 1)

        return max_len

