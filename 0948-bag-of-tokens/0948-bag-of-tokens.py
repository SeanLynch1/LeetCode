class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # score = 0
        # [100,200,300,400,500,600,1000], power = 100

        # score = 0: power = 100 - 100, score = 1
        # score = 1: power = 100 + 1000, score = 1

        # score = 0: power = 200 - 100, score = 1
        # score = 1: power = 100 + 1000, score = 0
        # score = 0: power = 1100 - 200, score = 1
        # score = 1: power = 900 - 300, score = 2
        # score = 2: power = 600 - 400, score = 3
        # score = 3: power = 200 + 600, score = 2
        # score = 2: power = 800 - 500, score = 3
        # score = 3

        max_score = 0
        score = 0
        tokens.sort()

        left = 0
        right = len(tokens) - 1

        while left <= right:
            
            cost = tokens[left]

            if power >= cost:
                power -= cost
                left += 1
                score += 1
                max_score = max(score, max_score)
            elif score >= 1:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break

        return max_score