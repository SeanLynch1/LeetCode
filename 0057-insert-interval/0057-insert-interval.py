class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        l, r = new
        placed = False
        res = []

        for start, end in intervals:
            # Case 1: interval is completely before new
            if end < l:
                res.append([start, end])
            
            # Case 2: interval is completely after new
            elif start > r:
                if not placed:
                    res.append([l, r])
                    placed = True
                res.append([start, end])

            # Case 3: overlap
            else:
                l = min(l, start)
                r = max(r, end)

        if not placed:
            res.append([l, r])

        return res