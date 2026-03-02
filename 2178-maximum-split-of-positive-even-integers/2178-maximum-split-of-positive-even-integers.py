class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
            
        ans = []
        cur = 2

        while finalSum >= cur:
            ans.append(cur)
            finalSum -= cur
            cur += 2

        # leftover always gets added to last
        ans[-1] += finalSum

        return ans