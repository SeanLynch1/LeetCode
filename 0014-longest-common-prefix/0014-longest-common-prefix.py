class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs = sorted(strs)
        prefix = strs[0]

        for s in strs:
            i = 0
            while i < len(s) and i <len(prefix) and prefix[i] == s[i]:
                i += 1

            prefix = prefix[0:i]

        return prefix