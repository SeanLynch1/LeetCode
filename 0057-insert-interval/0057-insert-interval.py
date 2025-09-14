class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key = lambda x : x[0])

        min_int = intervals[0][0]
        max_int = intervals[0][1]

        res = []
        for i in range(1, len(intervals)):

            if max_int >= intervals[i][0]:
                max_int = max(max_int, intervals[i][1])
            else:
                res.append([min_int, max_int])

                min_int = intervals[i][0]
                max_int = intervals[i][1]

        res.append([min_int, max_int])

        return res
        
