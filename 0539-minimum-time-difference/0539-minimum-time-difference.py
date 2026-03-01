class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        timePoints = [ _.split(":") for _ in timePoints]
        timePoints.sort()

        last_hours = int(timePoints[-1][0])
        last_mins = int(timePoints[-1][1])

        min_diff = float('inf')

        for i in range(len(timePoints)):

            hours = int(timePoints[i][0]) + 24
            mins = int(timePoints[i][1])

            min_diff = min(min_diff, (hours - last_hours) * 60 - last_mins + mins)

            last_hours = hours
            last_mins = mins

        return min_diff