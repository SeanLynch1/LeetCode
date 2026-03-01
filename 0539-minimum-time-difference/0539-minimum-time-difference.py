class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        timePoints = [[int(x) for x in _.split(":")] for _ in timePoints]
        timePoints.sort()

        last_hours = timePoints[0][0]
        last_mins = timePoints[0][1]

        min_diff = ((timePoints[0][0] + 24 - timePoints[-1][0]) * 60) - timePoints[-1][1] + timePoints[0][1]

        for i in range(1, len(timePoints)):

            hours = timePoints[i][0]
            mins = timePoints[i][1]

            min_diff = min(min_diff, (hours - last_hours) * 60 - last_mins + mins)

            last_hours = hours
            last_mins = mins

        return min_diff