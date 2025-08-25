from collections import defaultdict, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        found_letters = defaultdict(lambda: [0, 0])

        min_substring = ""
        count = 0
        sub_string = deque()

        for letter in t:
            a, b = found_letters[letter]
            found_letters[letter] = [0, b + 1]

        for i in range(len(s)):
            
            if s[i] in found_letters:
                if found_letters[s[i]][0] < found_letters[s[i]][1]:
                    count += 1

                found_letters[s[i]][0] += 1
                sub_string.append((s[i], i))

                while count == len(t):

                    if len(min_substring) > len(s[sub_string[0][1]:i+1]) or min_substring == "":
                        min_substring = s[sub_string[0][1]:i+1]

                    first_sub_letter = sub_string[0][0]

                    found_letters[first_sub_letter][0] -= 1

                    if found_letters[first_sub_letter][0] < found_letters[first_sub_letter][1]:
                        count -= 1
                    
                    # sets left to next value
                    sub_string.popleft()
                
        return min_substring
