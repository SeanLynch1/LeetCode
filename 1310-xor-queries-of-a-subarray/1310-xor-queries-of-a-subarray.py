class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        prefixes = [0]
        output = []

        for num in arr:
            prefixes.append(prefixes[-1] ^ num)

        for l, r in queries:
            output.append(prefixes[r + 1] ^ prefixes[l])

        return output