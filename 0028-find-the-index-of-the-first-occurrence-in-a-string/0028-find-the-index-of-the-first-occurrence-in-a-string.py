class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        # 1) Build LPS (Longest Prefix that is also Suffix) for needle
        lps = [0] * len(needle)
        prev = 0  # length of previous longest prefix-suffix
        i = 1

        while i < len(needle):
            if needle[i] == needle[prev]:
                prev += 1
                lps[i] = prev
                i += 1
            else:
                if prev != 0:
                    prev = lps[prev - 1]  # jump within needle
                else:
                    lps[i] = 0
                    i += 1

        # 2) KMP search
        i = 0  # index in haystack
        j = 0  # index in needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]  # don't move i back; shift j using lps
                else:
                    i += 1

        return -1
