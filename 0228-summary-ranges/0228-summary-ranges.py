class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        start = nums[0]
        res = []

        for i in range(len(nums)):
            if i < len(nums) - 1:
                if (nums[i] + 1) != nums[i + 1]:
                    if start == nums[i]:
                        res.append(str(nums[i]))
                    else:
                        res.append(f"{start}->{nums[i]}")
                    start = nums[i + 1]
            else:
                if start == nums[i]:
                    res.append(str(nums[i]))
                else:
                    res.append(f"{start}->{nums[i]}")

        
        return res