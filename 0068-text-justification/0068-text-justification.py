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

                    print(f"temp = {temp}")
                    for i in range(gap_slots):
                        temp[i] += " " * spaces_per_gap
                        if remaining_spaces > 0:
                            temp[i] += " "
                            remaining_spaces -= 1

                        print(f"t = {temp[i]}")
                else:
                    temp[-1] += " " * spaces_needed
                    
                line = "".join(temp)
                output.append(line)
                temp = [word]
                line_length = len(word)
                gap_slots = 1
                print("")

        # handling last line
        spaces_needed = maxWidth - line_length

        print(f"temp = {temp}")
        for i in range(len(temp)):
            print(f"t = {temp[i]}")
            
            if i == len(temp) - 1:
                print(f"spaces_needed = {spaces_needed}")
                temp[i] += " " * spaces_needed
            else:
                temp[i] += " "
                spaces_needed -= 1

            
            
        line = "".join(temp)
        output.append(line)

        for line in output:
            print(line)

        
        return output