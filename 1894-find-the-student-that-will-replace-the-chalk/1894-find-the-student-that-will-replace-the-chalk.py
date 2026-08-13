class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        # k = 25
        # [3, 4, 1, 2]
        # [0, 3, 7, 8, 10]

        prefix = [0]

        for val in chalk:
            prefix.append(prefix[-1] + val)

        remainder = k % prefix[-1]

        return bisect_right(prefix, remainder) - 1