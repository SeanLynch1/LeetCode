class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        idx = 1
        while idx < len(words):
            if Counter(words[idx]) == Counter(words[idx - 1]):
                words.pop(idx)
            else:
                idx += 1

        return words