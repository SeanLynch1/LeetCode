class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # kiloms # 0 1 2 3 4 5 6 7 8
        # length # 0 1 1 1 1 1 0 0 0
        # spaces # 4 2 2 2 2 2 4 4 4
        # length # 0 0 0 1 1 1 1 1 0
        # spaces # 4 4 4 1 1 1 1 1 4

        # space = [4,2,2,-1]

        trips = sorted(trips, key=lambda x: x[0])
        print(trips)

        curr_trip = 0

        spaces = [capacity] * 1000

        for passengers, start, stop in trips:
            
            for i in range(start, stop):
                spaces[i] -= passengers
                if spaces[i] < 0:
                    return False
            


        return True