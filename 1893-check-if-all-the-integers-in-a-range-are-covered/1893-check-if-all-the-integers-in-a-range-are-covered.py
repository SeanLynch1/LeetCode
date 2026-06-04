class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        ranges_set = [0] * 52

        for x,y in ranges:
            ranges_set[x] += 1
            ranges_set[y + 1] -= 1

        coverage = 0
        for i in range(right + 1):
            coverage += ranges_set[i]

            if i>= left and i<= right and coverage == 0:
                return False
        return True