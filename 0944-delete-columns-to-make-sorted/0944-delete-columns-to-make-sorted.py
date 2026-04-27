class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        rows = len(strs)
        cols = len(strs[0])
        total = 0
        grid = [[] for _ in strs]

        for i in range(len(strs)):
            for j in range(len(strs[i])):
                grid[i].append(strs[i][j])

        for c in range(cols):
            # search down the col
            last = strs[0][c]
            outcome = True

            for r in range(1, rows):    

                curr = strs[r][c]

                if curr < last:
                    outcome = False
                    break
                
                last = curr

            if not outcome:
                total += 1


        return total