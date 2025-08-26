class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = set()

        left, max_len = 0, 0
        

        for right in range(len(s)):
            
            if s[right] not in max_substring:
                max_substring.add(s[right])

                max_len = max(max_len, len(max_substring))
            else:
                while s[right] in max_substring:
                    max_substring.remove(s[left])
                    left += 1
                
                max_substring.add(s[right])

        
        return max_len