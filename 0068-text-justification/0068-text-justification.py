class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        curr_length = 0
        line = []
        res = []

        for w in words:
            if (len(w) + curr_length + len(line) - 1) < maxWidth:
                curr_length += len(w)
                line.append(w)
            else:
                spaces = maxWidth - curr_length

                for i in range(spaces):
                    line[i % ((len(line)-1) or 1)] += ' '

                res.append(''.join(line))

                curr_length = len(w)
                line = [w]

        for i in range(len(line)):
            if i != (len(line) -1):
                print(i)
                print(f"line length = {len(line)}")
                line[i] += ' '
                maxWidth -= 1
            else:
                print("hello")
                line[i] += (maxWidth - curr_length) * ' '
        
        res.append(''.join(line))

        print(res)

        return res