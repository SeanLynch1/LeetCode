class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}

        for idx, num in enumerate(nums):
            needed = target - num

            if needed in mapped:
                return [idx, mapped[needed]]

            mapped[num] = idx
            
