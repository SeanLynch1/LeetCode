class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        closest_sum = sum(nums[:3])

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                
                curr_sum = (nums[i] + nums[j] + nums[k])

                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum

                if curr_sum < target: 
                    j += 1
                elif curr_sum > target:
                    k -= 1
                else:
                    return target

        return closest_sum    
