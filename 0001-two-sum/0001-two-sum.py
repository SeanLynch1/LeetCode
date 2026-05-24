class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_copy = sorted(nums)

        left = 0
        right = len(nums_copy) - 1
        curr = -1

        while left < right:

            curr = nums_copy[left] + nums_copy[right]

            if curr == target:
                left = nums_copy[left]
                right = nums_copy[right]
                break

            if curr > target:
                right -= 1
            elif curr < target:
                left += 1

        output = []
        for idx, val in enumerate(nums):
            
            if val == left:
                output.append(idx)
                if len(output) == 2:
                    break
            elif val == right:
                output.append(idx)
                if len(output) == 2:
                    break


        return output