class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapped = defaultdict(list)

        for idx in range(len(nums)):
            mapped[nums[idx]].append(idx)

        nums.sort()

        left = 0
        right = len(nums) - 1
        curr = -1

        while left < right:

            curr = nums[left] + nums[right]

            if curr == target:
                return [mapped[nums[left]].pop(), mapped[nums[right]].pop()]

            if curr > target:
                right -= 1
            elif curr < target:
                left += 1