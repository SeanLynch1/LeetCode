class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        

        line = []
        characters = 0

        res = []


        for word in words:

            if characters + len(word) + len(line) <= maxWidth:
                line.append(word)
                characters += len(word)
            else:
                spaces = maxWidth - characters
                print("spaces = ", spaces)
                idx = 0
                for i in range(spaces):
                    line[idx % max(1, len(line) - 1)] += " "
                    idx += 1

                res.append(''.join(line))
                line = [word]
                characters = len(word)

        print(res)

        
        spaces = maxWidth - characters

        for i in range(len(line)):
            if i == len(line) - 1:
                line[i] += " " * spaces
            else:
                line[i] += " "
                spaces -= 1
            
        res.append(''.join(line))
        

        return res

        
                
