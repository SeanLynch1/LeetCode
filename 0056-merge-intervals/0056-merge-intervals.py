class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        output = []
        intervals.sort(key= lambda x : x[0])

        start = intervals[0][0]
        last = intervals[0][1]

        for i in range(1,len(intervals)):

            l, r = intervals[i][0], intervals[i][1]

            if l > last:
                output.append([start, last])
                start = l

            last = max(last, r)
            
        output.append([start, last])

        return output