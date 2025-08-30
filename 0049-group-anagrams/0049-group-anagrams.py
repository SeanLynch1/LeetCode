from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        parent_anagram = defaultdict(int)
        res = []

        for word in strs:
            letters = list(word)

            anagram = Counter(letters)

            key = tuple(sorted(anagram.items()))

            if key not in parent_anagram:
                parent_anagram[key] = len(res)
                res.append([])

            res[parent_anagram[key]].append(word)
            
        return res