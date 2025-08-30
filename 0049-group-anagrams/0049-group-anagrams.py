from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for word in strs:
            # Count letters in fixed-size array
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1

            # Use tuple as hashable key
            groups[tuple(count)].append(word)

        return list(groups.values())
