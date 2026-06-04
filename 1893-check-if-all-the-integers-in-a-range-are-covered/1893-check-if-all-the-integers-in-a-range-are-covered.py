class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        ranges_set = [None] * 51

        for x,y in ranges:
            for i in range(x,y+1):
                ranges_set[i] = i

        print(ranges_set)

        for i in range(left,right+1):
            if ranges_set[i] == None:
                return False

        return True