class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        # k = 4
        # [1,12,1 ,1 ,4 ,2 ,5 ,6 ,1]
        # [0,1 ,13,14,15,19,21,26,32,33]

        prefix = [0]
        output = 0

        for num in cardPoints:
            prefix.append(prefix[-1] + num)

        checks = k
        i = len(prefix) -1
        for j in range(checks,-1,-1):
            window = prefix[i] - prefix[k]
            output = max(output, prefix[-1] - window)
            k-=1
            i-=1

        return output