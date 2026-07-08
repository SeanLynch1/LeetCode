class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        res = [0] * (n + 1)

        for first, last, seats in bookings:
            res[first - 1] += seats
            res[last] -= seats

        curr = 0

        for i in range(len(res)):
            res[i] += curr
            curr = res[i]

        return res[:-1]