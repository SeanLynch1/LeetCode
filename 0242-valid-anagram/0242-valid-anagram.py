from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)
        
        print(s_dict)
        print(t_dict)

        print(len(t_dict - s_dict))
        return True if len(Counter(s) - Counter(t)) == 0 else False