class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        gap_slots = 0
        line_length = 0
        output = []
        temp = []

        for word in words:

            if line_length + gap_slots + len(word) <= maxWidth:
                temp.append(word)
                line_length += len(word)
                gap_slots += 1
            else:
                gap_slots -= 1
                spaces_needed = maxWidth - line_length

                if gap_slots > 0:
                    spaces_per_gap = spaces_needed // gap_slots
                    remaining_spaces = spaces_needed % gap_slots

                    for i in range(gap_slots):
                        temp[i] += " " * spaces_per_gap
                        if remaining_spaces > 0:
                            temp[i] += " "
                            remaining_spaces -= 1
                else:
                    temp[-1] += " " * spaces_needed
                    
                line = "".join(temp)
                output.append(line)
                temp = [word]
                line_length = len(word)
                gap_slots = 1

        # handling last line
        spaces_needed = maxWidth - line_length

        for i in range(len(temp)):
            if i == len(temp) - 1:
                temp[i] += " " * spaces_needed
            else:
                temp[i] += " "
                spaces_needed -= 1

        line = "".join(temp)
        output.append(line)

        return output