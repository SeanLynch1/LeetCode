from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        output = []
        ref_list = [False] * len(nums)

        def back_track(path: List) -> None:

            if len(path) == len(nums):
                output.append(path.copy())
                return

            for i in range(len(nums)):

                if not ref_list[i]:
                    path.append(nums[i])

                    ref_list[i] = True

                    back_track(path)

                    path.pop()
                    ref_list[i] = False

        back_track([])    

        return output