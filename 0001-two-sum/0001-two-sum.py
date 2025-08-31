from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_pos = defaultdict(list)

        for i in range(len(nums)):
            nums_pos[nums[i]].append(i)

        for num in nums:
            needed = target - num
            
            if needed in nums_pos:
                if num == needed and len(nums_pos[needed]) < 2:
                    continue

                idx_2 = nums_pos[needed].pop()
                idx_1 = nums_pos[num].pop()

                return [idx_1, idx_2]      