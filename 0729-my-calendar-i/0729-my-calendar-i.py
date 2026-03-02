import bisect

class MyCalendar:

    def __init__(self):
        self.events = []   # sorted by start

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_left(self.events, (start, end))

        # Check previous
        if i > 0 and self.events[i-1][1] > start:
            return False
        
        # Check next
        if i < len(self.events) and self.events[i][0] < end:
            return False

        self.events.insert(i, (start, end))
        return True