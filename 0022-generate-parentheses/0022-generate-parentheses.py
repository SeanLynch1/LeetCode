class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.output = []

        def back_track(path: List, opn, closed) -> None:
            
            if opn == 0 and closed == 0:
                print(path)
                self.output.append("".join(path.copy()))
                return

            if opn > 0:
                path.append("(")
                back_track(path, opn - 1, closed)
                path.pop()

            if closed > opn:
                path.append(")")
                back_track(path, opn, closed - 1)
                path.pop()


        back_track([],n,n)

        return self.output