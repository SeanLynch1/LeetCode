class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        

        waiting_list = defaultdict(list)
        total = 0
    
        for word in words:
            waiting_list[word[0]].append((word, 0))
        
        for i, letter in enumerate(s):

            if letter not in waiting_list:
                continue

            idx_list = waiting_list[letter]
            waiting_list[letter] = []

            for word, idx in idx_list:
                idx += 1

                if idx >= len(word):
                    total += 1
                else:
                    waiting_list[word[idx]].append((word,idx))

        return total