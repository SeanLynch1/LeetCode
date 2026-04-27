class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        rows = len(strs)
        cols = len(strs[0])
        total = 0

        for c in range(cols):
            # search down the col
            last = strs[0][c]
            outcome = False

            for r in range(1, rows):    

                curr = strs[r][c]

                if curr < last:
                    outcome = True
                    break
                
                last = curr

            if outcome:
                total += 1

        return total