class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # loop forward
        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i+1] = candies[i] + 1
        
        # loop backwards
        for i in range(n-1,0,-1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], candies[i] + 1)
        return sum(candies)