class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # kiloms # 0 1 2 3 4 5 6 7 8
        # length # 0 1 1 1 1 1 0 0 0
        # spaces # 4 2 2 2 2 2 4 4 4
        # length # 0 0 0 1 1 1 1 1 0
        # spaces # 4 4 4 1 1 1 1 1 4

        # space = [4,2,2,-1]

        spaces = [0] * 1001
        
        for passengers, start, stop in trips:
            spaces[start] += passengers
            spaces[stop] -= passengers

        curr = 0
        for change in spaces:
            curr += change
            if curr > capacity:
                return False
            
        return True