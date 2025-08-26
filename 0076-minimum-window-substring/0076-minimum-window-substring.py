from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_tracker = Counter(t)

        left, start, end = 0, 0, 0

        missing = len(t)

        # offset by 1 because end is exlusive when slicing, index represents end
        for right, char in enumerate(s, 1):

            if t_tracker[char] > 0:
                missing -= 1

            t_tracker[char] -= 1

            # if every letter in t is in use
            if missing == 0:
                while left < right and (t_tracker[s[left]] < 0):
                    t_tracker[s[left]] += 1
                    left += 1
                
                if right - left < end - start or end == 0:
                    start, end = left, right

                # exclude the left most letter for the next iteration
                t_tracker[s[left]] += 1
                left += 1
                missing += 1

        return s[start:end]