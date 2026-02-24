class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) < len(s):
            return False
            
        arr = [0] * 26

        for ch in s:
            alpha_idx = ord(ch) - ord('a')
            arr[alpha_idx] += 1

        for ch in t:
            alpha_idx = ord(ch) - ord('a')

            if arr[alpha_idx] == 0:
                return False

            arr[alpha_idx] -= 1
        
        return True