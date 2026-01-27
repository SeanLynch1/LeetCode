class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixes = [1]
        for i in range(1, len(nums)):
            prev_nums = nums[i - 1]
            prefixes.append(prev_nums * prefixes[-1])

        print(prefixes)
        last = 1
        for j in range(len(prefixes)-1,-1,-1):
            prefixes[j] *= last
            last *= nums[j]


        print(prefixes)

        return prefixes