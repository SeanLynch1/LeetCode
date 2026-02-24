class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        l, r = new
        res = []

        for start, end in intervals:
            # Case 1: interval is completely before new
            if end < l:
                res.append([start, end])
            
            # Case 2: interval is completely after new
            elif start > r:
                res.append([l, r])
                l = max(l, start)
                r = max(r, end)
            else:
                # Case 3: overlap
                l = min(l, start)
                r = max(r, end)

        res.append([l, r])

        return res