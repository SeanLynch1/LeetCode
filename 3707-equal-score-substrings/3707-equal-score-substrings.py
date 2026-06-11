class Solution:
    def scoreBalance(self, s: str) -> bool:
        
        prefixes = [0]
        for l in s:
            prefixes.append(prefixes[-1] + (ord(l) - ord('a') + 1))
        
        n = len(s)
        for i in range(n-1):
            left = prefixes[i + 1]
            right = prefixes[n] - prefixes[i + 1] 

            if left == right:
                return True

        return False