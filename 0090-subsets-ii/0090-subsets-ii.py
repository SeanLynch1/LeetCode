class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)

        def dfs(path: List, start: int) -> None:

            res.append(path.copy())

            for i in range(start, len(nums)):
                
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue

                path.append(nums[i])
                used[i] = True


                dfs(path, i + 1)

                path.pop()
                used[i] = False

        dfs([], 0)

        return res