class Solution:

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        # build a dict
        available = defaultdict(list)
        total = 0

        for i in range(len(s)):
            available[s[i]].append(i)

        for word in words:
            last_idx = -1

            for i in range(len(word)):
                
                letter = word[i]

                if letter in available:
                    arr = available[letter]

                    target = bisect_right(arr, last_idx)

                    if target == len(arr):
                        break
                    last_idx = arr[target]
                    if i == len(word) -1:
                        total += 1
                else:
                    break

        return total