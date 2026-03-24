class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # 1, 2
        # 1, 3
        # 1, 4
        # 2, 3
        # 3, 4
        # 4, 1

        # 1, 2, 3, 4

        # 1, 2, 3
        # 1, 2, 4
        # 1, 3, 4
        # 2, 3, 4
        output = []
        
        def back_track(start:int, curr: list) -> None:
            

            curr.append(start)

            if len(curr) == k:
                output.append(curr)
                return

            for val in range(start + 1, n + 1):
                pres = curr.copy()
                back_track(val, curr)
                curr = pres

            return 

        for i in range(1, n - k + 2):
            back_track(i, [])

        return output