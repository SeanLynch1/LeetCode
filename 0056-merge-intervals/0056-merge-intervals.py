class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)

        i = 0
        n = len(intervals)
        res = []

        while i < n:
            temp = intervals[i]
            j = i
            max_int = intervals[i][1]
            while j < n - 1 and max_int >= intervals[j + 1][0]:
                temp.extend(intervals[j + 1])
                max_int = max(max_int, intervals[j + 1][1])
                j += 1
            
            temp = sorted(temp)
            res.append([temp[0], temp[-1]])
            i = j + 1

        return res