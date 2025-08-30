from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        parent_anagram = {}
        res = []

        for word in strs:
            letters = list(word)

            anagram = Counter(letters)

            key = tuple(sorted(anagram.items()))

            if key not in parent_anagram:
                parent_anagram[key] = []
            
            parent_anagram[key].append(word)
                

        for key, value in parent_anagram.items():
            res.append(value)

        return res