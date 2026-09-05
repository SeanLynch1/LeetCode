class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        # k = 4
        # [1,12,1 ,1 ,4 ,2 ,5 ,6 ,1]
        # [0,1 ,13,14,15,19,21,26,32,33]

        prefix = [0]
        output = 0

        for num in cardPoints:
            prefix.append(prefix[-1] + num)

        print(f"prefix = {prefix}")
        checks = k
        i = len(prefix) -1
        for j in range(checks,-1,-1):
            print(f"k = {k},i = {i}")
            window = prefix[i] - prefix[k]
            print(f"window = {window}")
            total = prefix[-1] - window
            print(f"total = {total}")
            output = max(output, total)
            k-=1
            i-=1
            print("")

        return output