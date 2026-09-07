class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        order = sorted(score,reverse=True)
        mapping = defaultdict(str)

        for i in range(len(order)):
            num = order[i]
            if i == 0:
                mapping[num] = "Gold Medal"
            elif i == 1:
                mapping[num] = "Silver Medal"
            elif i == 2:
                mapping[num] = "Bronze Medal"
            else:
                mapping[num] = str(i + 1)

        output = [""] * len(score)

        for i, num in enumerate(score):
            output[i] = mapping[num]

        return output