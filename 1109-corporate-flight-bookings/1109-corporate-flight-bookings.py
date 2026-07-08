class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        prefixes = defaultdict(int)

        for first, last, seats in bookings:
            prefixes[first] += seats
            prefixes[last + 1] -= seats

        res = [0] * n
        curr = 0

        for i in range(len(res)):
            res[i] = (curr + prefixes[i + 1])
            curr = res[i]

        return res 