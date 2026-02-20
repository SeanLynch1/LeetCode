class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        output = []

        l = newInterval[0]
        r = newInterval[1]

        for i in range(len(intervals)):

            start, end = intervals[i][0], intervals[i][1]
            
            if end < l:
                output.append([start, end])
            elif start > r:
                output.append([l, r])
                
                l = start
                r = end
            else:
                l = min(start, l)
                r = max(end, r)

        output.append([l,r])

        return output
