class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for q in queries:
            curr = 0 
            count = 0
            for n in nums:
                if curr == q:
                    break

                if curr + n <= q:
                    curr += n
                    count += 1
            
            ans.append(count)

        return ans