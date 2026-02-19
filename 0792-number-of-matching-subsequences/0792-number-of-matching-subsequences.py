class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        total = 0
        idx_positions = defaultdict(list)

        for l, i in enumerate(s):
            idx_positions[i].append(l)

        for word in words:
            last_idx = -1

            for i in range(len(word)):
                letter = word[i]

                if letter not in idx_positions:
                    break

                idx_list = idx_positions[letter]
                nxt_idx = bisect_right(idx_list, last_idx)
                if nxt_idx == len(idx_list):
                    break
                
                last_idx = idx_list[nxt_idx]

                if i == len(word) - 1:
                    total += 1

        return total