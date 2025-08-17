class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, line, width = [], [], 0

        for w in words:
            if width + len(w) + len(line) > maxWidth:
                for i in range(maxWidth - width): line[i % (len(line) - 1 or 1)] += ' '
                res.append(''.join(line))
                line, width = [], 0
            line += [w]
            width += len(w)

        for i in range(len(line)):
            if i < len(line) -1 :
                line[i] += ' '
                print(line)
            else:
                line[i] += ' ' * (maxWidth - width - (i))
                print("last line = ", line)

        res.append(''.join(line))
        
        return res