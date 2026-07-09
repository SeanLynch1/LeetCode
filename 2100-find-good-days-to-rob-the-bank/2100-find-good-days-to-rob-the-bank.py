class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        # [ 5, 7, 7, 6, 3, 2, 3, 4, 1, 4, 1] time = 2
        # [-1, 0, 1, 2, 3, 4, 3, 2, 3, 2, 3]
        res = []
        n = len(security) 

        prefix = [0] * n
        curr = 0
        lst = security[0]

        for i in range(1, n):
            num = security[i]

            if num <= lst:
                curr += 1
            else:
                curr = 0

            prefix[i] = curr
            lst = num

        suffix = [0] * n
        curr = 0
        lst = security[-1]

        for i in range(n-1,time-1,-1):
            num = security[i]

            if num <= lst:
                curr += 1
            else:
                curr = 0

            suffix[i] = curr
            lst = num

            if i - time >= 0 and i + time < n and prefix[i] - prefix[i - time] == time and suffix[i] - suffix[i + time] == time:
                res.append(i)
        return res