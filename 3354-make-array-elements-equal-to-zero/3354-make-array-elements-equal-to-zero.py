class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        #  [1,0,2,0,3]
        #  [0,1,1,3,3,6]

        prefixes = [0]

        for num in nums:
            prefixes.append(prefixes[-1] + num)

        suffix = 0
        ans = 0

        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                diff = abs(prefixes[i] - suffix)
                if diff == 1:
                    ans += 1
                elif diff == 0:
                    ans += 2

            suffix += nums[i]
        return ans

