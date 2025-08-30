from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return False if len(s) != len(t) else True if len(Counter(s) - Counter(t)) == 0 else False