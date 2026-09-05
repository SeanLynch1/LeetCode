class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # [2,3,1,6,7,3,2]
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

        return output