class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True

        found = 0
        for l in t:
            print(l)
            if l == s[found]:
                print("found : ", l)
                found += 1
            if found == len(s):
                return True
        
        return False