class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        longest = 0
        curr_cost = 0

        left = 0
        right = 0
        n = len(s)

        while left < n:

            while right < n:
                diff = abs(ord(s[right]) - ord(t[right]))

                curr_cost += diff


                if curr_cost > maxCost:
                    break
                right += 1
                
            right += 1

            print(f"{s[left:right]}")
            longest = max(longest, right -1 - left)

            curr_cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1



        return longest