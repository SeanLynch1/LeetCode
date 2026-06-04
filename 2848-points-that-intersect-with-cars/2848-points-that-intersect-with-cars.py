class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        # 0 1 2 3 4 5 6 7
        #       -------
        #   ---------
        #         -------

        line = [0] * (102)

        for start, end in nums:
            line[start] += 1
            line[end + 1] -= 1

        curr = 0
        total = 0

        for num in line:
            
            curr += num
            if curr > 0:
                total += 1


        return total