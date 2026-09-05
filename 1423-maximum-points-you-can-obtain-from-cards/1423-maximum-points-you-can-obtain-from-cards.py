class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        if k == n:
            return sum(cardPoints)

        window = n - k
        total = sum(cardPoints)

        curr = sum(cardPoints[:window])
        min_sum = curr

        for r in range(window, n):
            curr += cardPoints[r] - cardPoints[r - window]
            min_sum = min(min_sum, curr)

        return total - min_sum