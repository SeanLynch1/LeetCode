class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []

        l = newInterval[0] # 2
        r = newInterval[1] # 5

        for i in range(len(intervals)):
            start = intervals[i][0] # 6
            end = intervals[i][1] # 9

            # 9 >= 1, 6 <= 5
            if end >= l and start <= r:
                l = min(l, start) # 1
                r = max(r, end) # 5
                
                print("yes")
            else:
                output.append([min(l, start), min(r, end)]) # 3, 10

                l = max(start, l) # 12
                r = max(r, intervals[i][1]) # 16
                
        output.append([l, r])

        return output
