class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        word_length = len(words[0])
        word_count = len(words)
        words_dict = defaultdict(int)

        for w in words:
            words_dict[w] += 1
        words = words_dict

        output = []

        for left in range(word_length):

            # start at idx 0, 1, 2 for word_length of 3
            seen = defaultdict(int)
            found = 0
            # right always moves forwards
            for right in range(left, len(s), word_length):
                
                curr_joined = s[right: right + word_length]
                print(f"curr_joined = {curr_joined}")

                if curr_joined in words:   
                    if seen[curr_joined] < words[curr_joined]:
                        
                        seen[curr_joined] += 1
                        found += 1

                        print(f"curr_joined = {curr_joined}, found = {found}")
                        if found == word_count:
                            print(f"{curr_joined} found!, adding {left} to output")
                            output.append(left)
                            left_word = s[left: left + word_length]
                            seen[left_word] -= 1
                            found -= 1
                            left += word_length
                            print(f"seen = {seen}, found = {found} \n")
                    else:
                        print(f"{curr_joined}, already in seen :/")
                        seen[curr_joined] += 1
                        found += 1

                        while seen[curr_joined] > words[curr_joined]:
                            left_word = s[left: left + word_length]
                            print(f"left_word = {left_word}")
                            seen[left_word] -= 1

                            left += word_length
                            found -= 1

                        print(f"left now = {left}")
                        print(f"seen = {seen}, found = {found} \n")
                else:
                    seen = defaultdict(int)
                    left = right + word_length
                    found = 0

                    print(f"{curr_joined}, not in seen :(")
                    print(f"seen = {seen}, found = {found} \n")


        
        return output


                    

