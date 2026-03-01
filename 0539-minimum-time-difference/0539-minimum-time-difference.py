class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        minutes = []
        for t in timePoints:
            h, m = map(int, t.split(":"))
            minutes.append(h * 60 + m)

        minutes.sort()
        last_mins = minutes[-1] - (24 * 60)

        min_diff = float('inf')

        for m in minutes:

            min_diff = min(min_diff, m - last_mins )

            last_mins = m

        return min_diff