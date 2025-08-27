from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t or len(t) > len(s):
            return ""

        t_tracker = Counter(t)

        missing = len(t)
        left, start, end = 0, 0, 0

        for right, char in enumerate(s, 1):
            
            if t_tracker[char] > 0:
                missing -= 1
            
            t_tracker[char] -= 1

            if missing == 0:
                print(f"right = {right}, left = {left}")
                print(f"s[left] = {s[left]}")
                print(t_tracker)
                while t_tracker[s[left]] < 0:
                    t_tracker[s[left]] += 1
                    left += 1

                if t_tracker[s[left]] == 0:
                    t_tracker[s[left]] += 1
                    missing += 1

                if right - left < end - start or end == 0:
                    start, end = left, right
                    print("updating word to ", s[start:end])
                
                left += 1

                print(t_tracker, "missing = ", missing, "left = ", left)
                print("\n")

        return s[start:end]
            

