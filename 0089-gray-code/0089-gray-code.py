class Solution:
    def grayCode(self, n: int) -> List[int]:
        

        # n = 3
        # 2^3

        # [0,1,2,3,4,5,6,7]

        # 0000 = 0
        # 0010 = 2

        # 0100 = 4
        # 0110 = 6
        # 0101 = 5
        # 0111 = 7

        # 0011 = 3
        # 0001 = 1

        res = [0]
        visited = set([0])

        def dfs(curr):
            if len(res) == (1 << n):
                return True

            for i in range(n):
                next_val = curr ^ (1 << i)  # flip ith bit

                if next_val not in visited:
                    visited.add(next_val)
                    res.append(next_val)

                    if dfs(next_val):
                        return True

                    visited.remove(next_val)
                    res.pop()

            return False

        dfs(0)
        return res