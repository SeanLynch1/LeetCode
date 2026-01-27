class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixes = [1]
        suffixes = [1]
        for i in range(1, len(nums)):
            prev_nums = nums[i - 1]
            prefixes.append(prev_nums * prefixes[-1])

        print(prefixes)
        for j in range(1, len(nums)):

            suffixes.append(nums[-j] * suffixes[-1])

        for k in range(0, len(prefixes)):
            prefixes[k] = prefixes[k] * suffixes[-k - 1]

        print(suffixes)

        return prefixes