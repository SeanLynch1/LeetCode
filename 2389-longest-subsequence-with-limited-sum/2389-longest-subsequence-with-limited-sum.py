class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        total = 0
        prefixes = []
        ans = []
        print(nums)
        for i, n in enumerate(nums):
            total += n
            prefixes.append(total)

        print(prefixes)
        for q in queries:
            ans.append(bisect_right(prefixes, q))

        return ans