class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        counts = defaultdict(int)
        max_freq = 0
        left = 0

        for right in range(len(s)):
            
            counts[s[right]] += 1
            max_freq = max(max_freq, counts[s[right]])

            while (right + 1 - left) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            longest = max(longest, right + 1 - left)

        return longest