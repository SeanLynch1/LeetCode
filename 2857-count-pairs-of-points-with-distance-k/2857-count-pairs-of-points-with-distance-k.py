class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        
        # k = 5

        # [
        # [1,2],
        # [4,2],
        # [1,3],
        # [5,2]
        # ]

        seen = defaultdict(int)
        ans = 0

        for x, y in coordinates:

            for dx in range(k + 1):

                dy = k - dx # dx + dy needs to equal k

                # find what needs to pair with dx and dy
                target_x = x ^ dx
                target_y = y ^ dy

                ans += seen[(target_x, target_y)]
            
            seen[(x, y)] += 1

        return ans
        '''total = 0

        for i in range(len(coordinates)):
            x1, y1 = coordinates[i]
            for j in range(i + 1, len(coordinates)):
                x2, y2 = coordinates[j]
                if (x1 ^ x2) + (y1 ^ y2) == k:
                    total += 1

        return total'''