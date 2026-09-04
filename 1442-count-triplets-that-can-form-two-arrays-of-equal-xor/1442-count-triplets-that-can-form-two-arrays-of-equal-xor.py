class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        # [2,3,1,6,7,3,2]
        # [0,2,1,0,6,1,2,0]

        counts = defaultdict(list)
        counts[0] = [0]
        prefixes = [0]

        output = 0

        for i, num in enumerate(arr):
            val = prefixes[-1] ^ num
            prefixes.append(val)

            if val in counts:
                for j in counts[val]:
                    output += i - j 

            counts[val].append(i + 1)


        return output