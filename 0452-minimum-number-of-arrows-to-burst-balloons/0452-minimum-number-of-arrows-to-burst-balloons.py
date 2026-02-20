class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        darts = 1
        points.sort(key=lambda x:x[1])

        last = points[0][1]

        for i in range(1, len(points)):
            
            l, r = points[i][0], points[i][1]

            if l > last:
                darts += 1
                last = r

                
        return darts