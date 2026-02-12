from bisect import bisect_right
from collections import defaultdict, Counter
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)

        total = 0
        freq = Counter(words)

        for w, count in freq.items():
            last = -1
            ok = True
            for ch in w:
                arr = pos.get(ch)
                if not arr:
                    ok = False
                    break
                j = bisect_right(arr, last)
                if j == len(arr):
                    ok = False
                    break
                last = arr[j]
            if ok:
                total += count

        return total
