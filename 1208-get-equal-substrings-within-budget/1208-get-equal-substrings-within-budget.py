class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        longest = 0
        curr_cost = 0

        left = 0
        right = 0
        n = len(s)

        for right in range(n):
            curr_cost += abs(ord(s[right]) - ord(t[right]))

            while curr_cost > maxCost:

                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            longest = max(longest, right + 1 - left)

        return longest