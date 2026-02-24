class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapping = defaultdict(int)

        for j in range(len(nums)):
            needed = target - nums[j]

            if needed in mapping and j != mapping[needed]:
                return [j, mapping[needed]]

            mapping[nums[j]] = j
            