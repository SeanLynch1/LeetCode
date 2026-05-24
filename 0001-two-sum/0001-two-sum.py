class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapped = defaultdict(list)

        for idx in range(len(nums)):
            mapped[nums[idx]].append(idx)

        for key in mapped:
            idx = mapped[key].pop()

            needed = target - key

            if needed in mapped:
                needed_list = mapped[needed]
                if needed_list != []:
                    return [idx, needed_list.pop()]