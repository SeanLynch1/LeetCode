class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        max_len = 0
        
        mapping = {0: 0}
        vowels = {'a','i','e','o','u'}

        n = len(s)
        xors = [0] * (n + 1)

        for i in range(n):
            
            letter = s[i]
            val = xors[i]

            if letter in vowels:
                val ^= ord(letter)
                xors[i + 1] = val

                if val not in mapping:
                    mapping[val] = i + 1
            else:
                xors[i + 1] = xors[i]

            if val in mapping:
                max_len = max(max_len, i - mapping[val] + 1)

        return max_len

