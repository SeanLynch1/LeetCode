class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = 0
        h = len(haystack)
        n = len(needle)
        letter = 0

        while right < h:
            if haystack[right] == needle[letter]:
                letter += 1
                right += 1

                if letter == n:
                    return left
            else:
                letter = 0
                left += 1
                right = left

        return -1