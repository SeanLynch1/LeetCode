class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        

        deletions = 0
        rows = len(strs) - 1
        cols = len(strs[0])

        resolved_words = [False] * rows


        for col in range(cols):

            bad = False

            for i in range(rows):
                # compare forwards
                if not resolved_words[i]:
                    if strs[i][col] > strs[i + 1][col]:
                        bad = True
                        break
            
            if bad:
                deletions += 1
                continue

            for i in range(rows):
                if strs[i][col] < strs[i + 1][col]:
                    resolved_words[i] = True

        return deletions