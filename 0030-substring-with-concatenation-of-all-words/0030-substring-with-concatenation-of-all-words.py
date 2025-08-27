from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        word_tracker = Counter(words)

        res = []

        word_len = len(words[0])

        for i in range(0, word_len):
            count = 0
            left = i
            word_window = defaultdict(int)

            for j in range(i,len(s),word_len):
                curr_word = s[j:j+word_len]

                if curr_word not in word_tracker:
                    # reset everything
                    count = 0
                    left = j + word_len
                    word_window = defaultdict(int)
                    continue

                # update word_window with current_word
                word_window[curr_word] += 1
                count += 1

                # check if the curr_word count exceeds its allowed count
                while word_window[curr_word] > word_tracker[curr_word]:
                    left_word = s[left:left+word_len]
                    word_window[left_word] -= 1
                    count -= 1

                    left += word_len

                if count == len(words):
                    res.append(left)


        return res

                    