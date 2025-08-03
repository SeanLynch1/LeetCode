class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # loop forward
        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i+1] = candies[i] + 1
        print(candies)
        
        # loop backwards
        for i in range(n-1,0,-1):
            if ratings[i-1] > ratings[i]:
                maximum  = max(candies[i-1], candies[i] + 1)
                candies[i-1] = maximum
        print(candies)
        return sum(candies)