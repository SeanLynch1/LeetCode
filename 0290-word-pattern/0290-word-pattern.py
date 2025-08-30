class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(" ")
        print(words)
        if len(words) != len(pattern):
            return False

        pattern_to_words = {}
        words_to_pattern = {}

        for i in range(len(pattern)):
            if (words[i] in words_to_pattern and words_to_pattern[words[i]] != pattern[i]) or (pattern[i] in pattern_to_words and pattern_to_words[pattern[i]] != words[i]):
                return False
            
            pattern_to_words[pattern[i]] = words[i]
            words_to_pattern[words[i]] = pattern[i]


        return True