class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        idx = {'a':0,'e':1,'i':2,'o':3,'u':4}
        total = 0
        n = len(word)

        for i in range(n):
            mask = 0
            right = i
            while right < n and word[right] in idx:
                mask |= 1 << idx[word[right]]
                if mask == 0b11111:
                    total += 1
                right += 1

        return total
