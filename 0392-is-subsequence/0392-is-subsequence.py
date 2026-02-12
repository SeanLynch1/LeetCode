class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        idx = 0
        curr = s[idx]

        for i in range(len(t)):

            if t[i] == curr:
                
                idx += 1
                if idx == len(s):
                    return True
                curr = s[idx]

        return False