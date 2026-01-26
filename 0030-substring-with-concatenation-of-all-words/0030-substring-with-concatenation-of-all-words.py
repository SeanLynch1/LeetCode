class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        word_length = len(words[0])
        word_count = len(words)
        words_dict = defaultdict(int)

        for w in words:
            words_dict[w] += 1

        output = []

        for left in range(word_length):

            # start at idx 0, 1, 2 for word_length of 3
            seen = defaultdict(int)
            found = 0
            # right always moves forwards
            for right in range(left, len(s), word_length):
                
                curr_joined = s[right: right + word_length]

                if curr_joined in words_dict:   
                    if seen[curr_joined] < words_dict[curr_joined]:
                        
                        seen[curr_joined] += 1
                        found += 1

                        if found == word_count:
                            output.append(left)
                            left_word = s[left: left + word_length]
                            seen[left_word] -= 1
                            found -= 1
                            left += word_length
                    else:
                        seen[curr_joined] += 1
                        found += 1

                        while seen[curr_joined] > words_dict[curr_joined]:
                            left_word = s[left: left + word_length]
                            seen[left_word] -= 1

                            left += word_length
                            found -= 1

                else:
                    seen = defaultdict(int)
                    left = right + word_length
                    found = 0

        
        return output


                    

