class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        total = 0
        prefixes = []
        ans = []
        
        for i, n in enumerate(nums):
            total += n
            prefixes.append(total)

        for q in queries:
            ans.append(bisect_right(prefixes, q))

        return ans