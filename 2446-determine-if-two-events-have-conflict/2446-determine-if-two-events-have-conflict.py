class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        time_1 = int(event1[0][:2] + event1[0][3:])
        time_2 = int(event1[1][:2] + event1[1][3:])

        time_3 = int(event2[0][:2] + event2[0][3:])
        time_4 = int(event2[1][:2] + event2[1][3:])

        print(time_1, time_2, time_3, time_4)

        return (time_2 >= time_3 and time_3 >= time_1) or (time_2 >= time_3 and time_4 >= time_1)