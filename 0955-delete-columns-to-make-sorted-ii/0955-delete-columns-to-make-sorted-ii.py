from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        rows = len(strs)
        cols = len(strs[0])

        # resolved[i] means:
        # strs[i] < strs[i + 1] has already been confirmed
        resolved = [False] * (rows - 1)

        deletions = 0

        # process columns left -> right
        for col in range(cols):

            # check whether keeping this column breaks ordering
            bad = False

            for row in range(rows - 1):

                # only compare unresolved pairs
                if not resolved[row]:
                    if strs[row][col] > strs[row + 1][col]:
                        bad = True
                        break

            # must delete this column
            if bad:
                deletions += 1
                continue

            # otherwise keep the column
            # and mark newly resolved pairs
            for row in range(rows - 1):

                if strs[row][col] < strs[row + 1][col]:
                    resolved[row] = True

        return deletions