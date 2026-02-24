class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []
        mapping = {}
        
        for word in strs:
            key = ''.join(sorted(word))

            if key in mapping:
                output[mapping[key]].append(word)
            else:
                mapping[key] = len(mapping)
                output.append([word])

        return output 