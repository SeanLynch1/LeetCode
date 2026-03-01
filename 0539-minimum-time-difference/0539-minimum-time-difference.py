class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        timePoints = [[int(x) for x in t.split(":")] for t in timePoints]
        timePoints.sort()

        last_hours = timePoints[-1][0]
        last_mins = timePoints[-1][1]

        min_diff = float('inf')

        for h, m in timePoints:
            hours = h + 24
            mins = m

            min_diff = min(min_diff, (hours - last_hours) * 60 - last_mins + mins)

            last_hours = hours
            last_mins = mins

        return min_diff