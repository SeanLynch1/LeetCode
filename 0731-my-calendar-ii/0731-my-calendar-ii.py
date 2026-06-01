class MyCalendarTwo:

    def __init__(self):
        # [[10, 20], [50, 60]]
        # [[10, 40], ]

        self.bookings = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> bool:
        
        '''for slot in self.overlaps:
            if startTime >= slot[0] and startTime < slot[1]:
                return False
            elif endTime > slot[0] and endTime <= slot[1]:
                return False
            elif startTime <= slot[0] and endTime >= slot[1]:
                return False
            
        min_left = startTime
        max_right = endTime
        #[10, 20] [9,21]
        for slot in self.bookings:
            if startTime <= slot[0] and endTime >= slot[1]:
                self.overlaps.append([slot[0], slot[1]])
                
            elif startTime >= slot[0] and startTime < slot[1] or endTime > slot[0] and endTime <= slot[1]:
                min_left = max(startTime, slot[0])
                max_right = min(endTime, slot[1])
                self.overlaps.append([min_left, max_right])

        self.bookings.append([startTime, endTime])'''
        self.bookings[startTime] += 1
        self.bookings[endTime] -= 1
        active = 0

        for key in sorted(self.bookings):
            val = self.bookings[key]
            active += val

            if active > 2:
                self.bookings[startTime] -= 1
                self.bookings[endTime] += 1
                return False
        return True

'''[[1,20],[5,15],[13,17],[18,20],[0,21]]

    {
    0: 1,
    1: 1,
    5: 1,
    13: 1,
    15: -1,
    17: -1,
    18: 1,    
    20: -2,
    21: -1}
'''
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)