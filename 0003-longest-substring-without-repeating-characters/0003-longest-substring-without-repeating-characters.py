class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_substring = 0
        found = set()
        left = 0
        

        for right in range(len(s)):

            curr = s[right]

            if curr not in found:
                found.add(curr)
            else:
                max_substring = max(max_substring, right - left)

                while curr in found:
                    print(found)
                    found.remove(s[left])
                    left += 1

                found.add(curr)

        max_substring = max(max_substring, right - left + 1)

        return max_substring