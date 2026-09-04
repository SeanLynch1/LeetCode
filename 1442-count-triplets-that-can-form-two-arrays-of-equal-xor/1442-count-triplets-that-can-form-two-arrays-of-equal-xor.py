class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        # [2,3,1,6,7,3]
        # [0,2,1,0,6,1,2]
        # [0,3,2,4,3,0]
        # [0,1,7,0,3]

        output = 0
        prefixes = [0]

        for num in arr:
            prefixes.append(prefixes[-1] ^ num)

        for i in range(len(arr)):

            for j in range(i + 1, len(arr)):

                if prefixes[i] == prefixes[j + 1]:
                    output += j - i 

        return output