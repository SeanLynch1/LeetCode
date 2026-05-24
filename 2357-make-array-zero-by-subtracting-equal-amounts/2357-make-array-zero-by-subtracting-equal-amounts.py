class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        ops = 0
        positives = [num for num in nums if num > 0]
        if not positives:
            return 0

        lowest = min(positives)
        print(positives)
        
        while True:

            if positives:
                next_lowest = 0
                for i in range(len(positives)):

                    positives[i] -= lowest

                    if next_lowest == 0:
                        if positives[i] > 0:
                            next_lowest = positives[i]
                    else:
                        if positives[i] > 0:
                            next_lowest = min(next_lowest, positives[i])

                lowest = next_lowest
                positives = [num for num in positives if num > 0]
                print(positives)
                ops += 1

            else:
                return ops