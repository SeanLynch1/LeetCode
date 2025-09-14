class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        res = []
        j = 0
        min_int = intervals[0][0]
        max_int = intervals[0][1]

        for j in range(len(intervals) - 1):
            if max_int >= intervals[j + 1][0]:
                max_int = max(max_int, intervals[j + 1][1])
            else:
                res.append([min_int, max_int])
                min_int = intervals[j+1][0]
                max_int = intervals[j+1][1]

        res.append([min_int, max_int])
        return res