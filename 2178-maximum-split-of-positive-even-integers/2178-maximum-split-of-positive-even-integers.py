class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
            
        output = []
        total = 0
        mid_point = finalSum // 2 + 2

        for i in range(2, mid_point + 2, 2):
            total += i
            if total > finalSum:
                
                output[-1] += i - (total - finalSum)
                return output
            
            output.append(i)

            if total == finalSum:
                return output

        return output