from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        parent_anagram = defaultdict(list)
        res = []

        for word in strs:
            parent_anagram[tuple(sorted(Counter(list(word)).items()))].append(word)

        for key, value in parent_anagram.items():
            res.append(value)

        return res