from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        leds = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        res = []

        def dfs(i, count, hour, minute):
            # invalid state
            if hour >= 12 or minute >= 60:
                return

            # base case
            if count == turnedOn:
                res.append(f"{hour}:{minute:02d}")
                return

            if i == len(leds):
                return

            # choose current LED
            if i < 4:
                dfs(i + 1, count + 1, hour + leds[i], minute)
            else:
                dfs(i + 1, count + 1, hour, minute + leds[i])

            # skip current LED
            dfs(i + 1, count, hour, minute)

        dfs(0, 0, 0, 0)
        return res