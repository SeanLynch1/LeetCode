class Solution:
    def reverseWords(self, s: str) -> str:
        #return ' '.join(s.strip().split()[-1:-1:-1])

        s = s.strip()
        res = []

        right = len(s)

        for i in range(len(s)-1,-1,-1):
            
            if s[i] == ' ':
                word = s[i + 1:right]
                if len(word) > 0:
                    res.append(word)

                right = i 
        
        if right > i:
            res.append(s[i:right])
            
        return ' '.join(res)


