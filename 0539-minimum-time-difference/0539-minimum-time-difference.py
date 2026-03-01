class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        minutes = []
        for t in timePoints:
            h, m = map(int, t.split(":"))
            minutes.append(h * 60 + m)

        minutes.sort()
        min_diff = float('inf')

        # Check adjacent differences
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        # Wrap-around: last → first across midnight
        min_diff = min(min_diff, 1440 - (minutes[-1] - minutes[0]))

        return min_diff