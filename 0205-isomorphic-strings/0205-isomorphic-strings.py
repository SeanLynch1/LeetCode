from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        unique_s = {}

        for char in s:
            if char not in unique_s:
                unique_s[char] = 1

        s_mapping = {}

        mapped_word = []

        for i in range(len(t)):
            if t[i] not in s_mapping:
                if unique_s[s[i]] > 0:
                    s_mapping[t[i]] = s[i]
                    unique_s[s[i]] -= 1
                else:
                    return False

            mapped_word.append(s_mapping[t[i]])

        print("mapped word = ", ''.join(mapped_word))
        if ''.join(mapped_word) == s:
            return True
        else:
            return False

