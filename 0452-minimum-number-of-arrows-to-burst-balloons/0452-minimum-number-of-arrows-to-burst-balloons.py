class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        arrows = 1
        points.sort(key= lambda x : x[1])
        aligned = [points[0]]

        print(points)

        for i in range(1, len(points)):
            max_int = aligned[-1][1]

            if max_int >= points[i][0]:
                aligned[-1][1] = min(max_int, points[i][1])
            else:
                aligned = [points[i]]
                arrows += 1

        return arrows