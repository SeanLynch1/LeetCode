class Solution:
    def pivotInteger(self, n: int) -> int:
        
        prefixes = [0]
        # [1,3,6,10,15,21,28,36]
        # [8,15,21,26,30,33,35,36]

        for i in range(1, n + 1):
            prefixes.append(prefixes[-1]+i)

        suffixes = 0

        for i in range(n,-1,-1):
            suffixes += i

            if suffixes == prefixes[i]:
                return i

        return -1
        