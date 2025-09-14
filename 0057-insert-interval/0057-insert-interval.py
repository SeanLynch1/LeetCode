class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key = lambda x : x[0])

        print(intervals)
        min_int = intervals[0][0]
        max_int = intervals[0][1]

        res = []
        for i in range(len(intervals) - 1):

            if max_int >= intervals[i + 1][0]:
                max_int = max(max_int, intervals[i + 1][1])
            else:
                res.append([min_int, max_int])

                min_int = intervals[i + 1][0]
                max_int = intervals[i + 1][1]

        res.append([min_int, max_int])

        return res
        
