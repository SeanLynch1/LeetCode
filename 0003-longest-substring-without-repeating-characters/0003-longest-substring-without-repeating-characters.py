class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, res, characters = 0, 0, set()

        for right in s:
            while right in characters:
                characters.remove(s[left])
                left += 1

            characters.add(right)
            res = max(res, len(characters))


        return res