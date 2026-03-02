class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        
        for s, e in self.calendar:
            if max(startTime, s) < min(endTime, e):
                return False

        self.calendar.append([startTime, endTime])

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)