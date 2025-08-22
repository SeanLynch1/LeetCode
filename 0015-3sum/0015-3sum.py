class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        i = 0

        while i < len(nums) and nums[i] <= 0:

            if i > 0 and nums[i] == nums[i-1]:
                print(f"i = i -1, setting i to {i+1}")
                i+= 1
                continue
            
            # look for combos
            j = i + 1
            k = len(nums) - 1
            target = 0 - nums[i]

            while j < k:
                total = nums[j] + nums[k]
                if total == target:
                    
                    if res: 
                        if (nums[j] == res[-1][1] and nums[k] == res[-1][2]):
                            k -= 1
                            continue
                        
                    res.append([nums[i],nums[j], nums[k]])
                    
                    k -= 1
                elif total > target:
                    k -= 1
                else:
                    j += 1

            i += 1

        return res
