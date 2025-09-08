class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        # forward pass
        for i in range(1, len(ratings)):
            
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i - 1] + 1

        # backwards pass
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1] and candies[j] <= candies[j + 1]:
                candies[j] = candies[j + 1] + 1
            
        return sum(candies)