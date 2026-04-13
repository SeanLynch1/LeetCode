class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def validate(val):
            # rule 1: no leading zeroes

            # rule 2: >= 0 AND <= 255

            if len(val) > 1 and val[0] == "0" or int(val) > 255:
                return False

            return True

        def dfs(path: List, start: int) -> None:
            
            if len(path) == 4 and start == len(s):
                res.append(".".join(path))
                return

            if len(path) > 4:
                return

            remaining_chars = len(s) - start
            remaining_slots = 4 - len(path)

            if remaining_chars < remaining_slots or remaining_chars > remaining_slots * 3:
                return

            for i in range(start, min(len(s), start + 3)):
                curr = s[start:i + 1]
                if validate(curr):

                    path.append(curr)
                    dfs(path, i + 1)
                    path.pop()
                

        dfs([], 0)

        return res