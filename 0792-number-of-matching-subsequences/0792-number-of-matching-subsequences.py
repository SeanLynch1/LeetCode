class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        total = 0
        idx_positions = defaultdict(list)

        for l, i in enumerate(s):

            idx_positions[i].append(l)

        for word in words:
            last_idx = 0

            for i in range(len(word)):
                letter = word[i]

                if letter not in idx_positions:
                    break

                nxt_idx = bisect_left(idx_positions[letter], last_idx)
                if nxt_idx >= len(idx_positions[letter]) :
                    break
                
                last_idx = idx_positions[letter][nxt_idx] + 1

                if i == len(word) - 1:
                    total += 1

        return total