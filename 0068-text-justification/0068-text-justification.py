class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        width, line, res = 0, [], []

        for w in words:
            if width + len(w) + len(line) > maxWidth:
                for i in range(maxWidth - width):
                    line[i % (len(line) - 1 or 1)] += ' '
                res.append(''.join(line))
                width, line = 0, []

            width += len(w)
            line.append(w)

        '''
        line_len = len(line)

        for i in range(line_len):
            if i < line_len - 1:
                line[i] += ' '
            else:
                line += ' ' * ((maxWidth - width) - (len(line) - 1)) 

        res.append(''.join(line))'''

        res.append(' '.join(line).ljust(maxWidth))
        return res
