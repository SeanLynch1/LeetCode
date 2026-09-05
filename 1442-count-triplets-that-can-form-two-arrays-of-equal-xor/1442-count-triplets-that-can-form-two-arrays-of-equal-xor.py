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

        '''# [2,3,1,6,7,3,2]
        # [0,2,1,0,6,1,2,0]

        # [2,4,1,6,7,3,2]
        # [0,2,6,7,1,6,5,7]

        counts = defaultdict(int)
        index_sum = defaultdict(int)

        xor = 0
        output = 0

        counts[0] = 1
        index_sum[0] = 0

        for i, num in enumerate(arr):
            xor ^= num

            output += (i * counts[xor]) - index_sum[xor]

            counts[xor] += 1
            index_sum[xor] += i + 1

        return output'''