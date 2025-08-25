from collections import defaultdict, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t:
            return ""


        found_letters = defaultdict(lambda: [0, 0])

        count = 0
        sub_string = deque()

        start = 0
        end = 0

        for letter in t:
            a, b = found_letters[letter]
            found_letters[letter] = [0, b + 1]

        for right, char in enumerate(s, 0):
            
            if char in found_letters:
                if found_letters[char][0] < found_letters[char][1]:
                    count += 1

                found_letters[char][0] += 1
                sub_string.append([char, right])

                while count == len(t):
                    
                    if (end - start) > (right - sub_string[0][1]) or (end - start) == 0:
                        start = sub_string[0][1]
                        end = right + 1

                    first_sub_letter = sub_string[0][0]

                    found_letters[first_sub_letter][0] -= 1

                    if found_letters[first_sub_letter][0] < found_letters[first_sub_letter][1]:
                        count -= 1
                    
                    # sets left to next value
                    sub_string.popleft()
                
        return s[start:end]
