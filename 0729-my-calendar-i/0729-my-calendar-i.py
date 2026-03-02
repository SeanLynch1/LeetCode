class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        
        for s, e in self.calendar:
            if startTime >= s and startTime < e or endTime > s and endTime <= e or startTime <= s and endTime >= e:
                return False

        self.calendar.append([startTime, endTime])

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)