class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        darts = 1
        intervals.sort(key= lambda x :x[1])
        last = intervals[0][1]

        print(intervals)

        for i in range(1, len(intervals)):

            l, r = intervals[i][0], intervals[i][1]

            if l >= last:
                darts += 1
                last = r


        return len(intervals) - darts