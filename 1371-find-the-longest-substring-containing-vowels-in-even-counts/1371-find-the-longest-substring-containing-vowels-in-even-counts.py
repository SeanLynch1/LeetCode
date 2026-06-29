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

        mapping = {0: -1}
        vowels = {'a':1,'i':2,'e':3,'o':4,'u':5}
        val = 0

        for i in range(len(s)):
            
            letter = s[i]

            if letter in vowels:
                val ^= 1 << vowels[letter]

            if val not in mapping:
                mapping[val] = i
            else:
                max_len = max(max_len, i - mapping[val])

        return max_len