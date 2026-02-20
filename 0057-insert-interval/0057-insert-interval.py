class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        s, e = newInterval
        placed = False

        for start, end in intervals:
            # Case 1: current interval is completely before newInterval (no overlap)
            if end < s:
                res.append([start, end])

            # Case 2: current interval is completely after newInterval (no overlap)
            elif start > e:
                if not placed:
                    res.append([s, e])   # place merged newInterval once
                    placed = True
                res.append([start, end])

            # Case 3: overlap → merge with newInterval
            else:
                s = min(s, start)
                e = max(e, end)

        # If newInterval goes at the very end
        if not placed:
            res.append([s, e])

        return res