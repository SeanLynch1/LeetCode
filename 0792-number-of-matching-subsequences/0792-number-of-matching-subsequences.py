from collections import defaultdict, deque
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(deque)
        matched = 0

        # Seed buckets by the first character each word is waiting for
        for w in words:
            waiting[w[0]].append((w, 0))  # (word, index_of_next_char_to_match)

        # Stream through s and advance all words waiting on each character
        for ch in s:
            bucket = waiting[ch]
            waiting[ch] = deque()  # clear this bucket; we'll refill as we advance states

            while bucket:
                w, i = bucket.popleft()
                i += 1  # we matched w[i] == ch, so move to next needed character

                if i == len(w):
                    matched += 1
                else:
                    waiting[w[i]].append((w, i))

        return matched
