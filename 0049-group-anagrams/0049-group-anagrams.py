from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        parent_anagram = defaultdict(list)
        res = []

        for word in strs:
            letters = list(word)

            anagram = Counter(letters)

            key = frozenset(anagram.items())

            parent_anagram[key].append(word)

        for key, value in parent_anagram.items():
            res.append(value)

        return res