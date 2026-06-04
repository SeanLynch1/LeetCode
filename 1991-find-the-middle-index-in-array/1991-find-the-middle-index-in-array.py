class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        suffixes = [0] * (len(nums) + 1)

        for i in range(len(nums)-1,-1,-1):
            suffixes[i] = suffixes[i + 1] + nums[i]

        print(suffixes)
        prefixes = 0

        for i in range(0, len(nums)):

            if suffixes[i + 1] == prefixes:
                return i
            
            prefixes += nums[i]


        return -1