class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapping = defaultdict(list)
        output = []

        for word in strs:
            
            arr = [0] * 26
            for ch in word:
                arr_idx = ord('a') - ord(ch)
                arr[arr_idx] += 1

            mapping[tuple(arr)].append(word)

        return list(mapping.values())