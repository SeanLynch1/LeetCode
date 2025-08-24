from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        word_length = len(words[0])
        indexes = []

        # this is to offset start position, depending on where word ordering falls in string
        for i in range(word_length):
            start = i
            word_window = defaultdict(int)
            words_used = 0

            for j in range(i,len(s), word_length):
                curr_word = s[j:j+word_length]


                # if we run into a substring that is not a word in words
                if curr_word not in word_count:
                    start = j + word_length
                    word_window = defaultdict(int)
                    words_used = 0
                    continue

                word_window[curr_word] += 1
                words_used += 1

                while word_window[curr_word] > word_count[curr_word]:

                    word_window[s[start:start+word_length]] -= 1
                    start += word_length
                    words_used -= 1

                if words_used == len(words):
                    indexes.append(start)

        return indexes

