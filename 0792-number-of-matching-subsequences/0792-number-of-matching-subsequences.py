class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        waiting = defaultdict(deque)
        total = 0
        for w in words:

            waiting[w[0]].append((w,0))

        for ch in s:
            
            bucket = waiting[ch]
            # clear waiting, we may add to this key later
            waiting[ch] = deque()

            for word, idx in bucket:
                
                idx += 1

                if idx == len(word):
                    total += 1
                else:
                    waiting[word[idx]].append((word, idx))

        return total

