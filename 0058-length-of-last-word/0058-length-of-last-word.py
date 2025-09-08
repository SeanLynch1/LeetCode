class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        split = s.split()

        return len(split[-1])