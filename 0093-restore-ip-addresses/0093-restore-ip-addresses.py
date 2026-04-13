class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def validate(val):
            print(f"val = {val}")
            num = int(val)

            if len(val) > 1 and val[0] == "0":
                return False

            if not (num >= 0 and num <= 255):
                return False

            return True



        def dfs(path: List, start: int) -> None:
            
            if len(path) == 4 and start == len(s):
                print(f"path = {".".join(path.copy())}")
                res.append(".".join(path.copy()))
                return


            # rule 1: no leading zeroes

            # rule 2: >= 0 AND <= 255

            for i in range(start, min(len(s), start + 3)):
                print(f"s[{i}] = {s[i]}")
                curr = s[start:i + 1]
                if validate(curr):
                    print(f"curr = {curr}")

                    path.append(curr)
                    dfs(path, i + 1)
                    path.pop()
                

        dfs([], 0)

        return res