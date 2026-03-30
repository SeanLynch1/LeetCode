class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.opn = n
        self.closed = n
        self.output = []

        def back_track(path: List) -> None:
            
            if self.opn == 0 and self.closed == 0:
                print(path)
                self.output.append("".join(path.copy()))
                return

            if self.opn > 0:
                path.append("(")
                self.opn -= 1
                back_track(path)
                path.pop()
                self.opn += 1

            if self.closed > self.opn:
                path.append(")")
                self.closed -= 1
                back_track(path)
                path.pop()

                self.closed += 1

            return


        back_track([])

        return self.output