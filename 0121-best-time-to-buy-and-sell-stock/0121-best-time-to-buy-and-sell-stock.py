class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_prof = 0
        lowest = prices[0]

        for i in range(len(prices)):

            lowest = min(lowest, prices[i])

            diff = prices[i] - lowest
            if  diff > max_prof:
                max_prof = diff

        return max_prof
