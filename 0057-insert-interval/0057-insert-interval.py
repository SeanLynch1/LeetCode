class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key = lambda x : x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            max_int = res[-1][1]
            if max_int >= intervals[i][0]:
                res[-1][1] = max(max_int, intervals[i][1])
            else:
                res.append([intervals[i][0], intervals[i][1]])

        return res