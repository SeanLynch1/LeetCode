class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        years = []

        for birth, death in logs:
            years.append([birth, 1])
            years.append([death, -1])

        years.sort(key=lambda x: (x[0], x[1]))

        ans = years[0][0]
        max_curr = 1
        curr = 0

        for slot in years:
            curr += slot[1]
            if curr > max_curr:
                max_curr = curr
                ans = slot[0]
        return ans