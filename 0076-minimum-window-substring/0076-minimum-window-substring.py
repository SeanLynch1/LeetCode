class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = Counter(t)

        left = 0
        start = 0
        missing = len(t)
        min_len = float('inf')

        for right in range(len(s)):
            c = s[right]

            if need[c] > 0:
                missing -= 1

            need[c] -= 1

            while missing == 0:
                if min_len > right - left + 1:
                    min_len = right - left + 1
                    start = left

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1

                left += 1

        return s[start:start + min_len] if min_len != float('inf') else ""