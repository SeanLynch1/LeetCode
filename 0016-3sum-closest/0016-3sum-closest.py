class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        closest_sum = sum(nums[:3])
        closest_distance = abs(target - closest_sum)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                
                remaining = target - nums[i]


                curr_sum = (nums[i] + nums[j] + nums[k])


                if abs(target - curr_sum) < closest_distance:
                    closest_distance = abs(target - curr_sum)
                    closest_sum = curr_sum

                if nums[j] + nums[k] < remaining: 
                    j += 1
                elif nums[j] + nums[k] > remaining:
                    k -= 1
                else:
                    return target

                



        return closest_sum    
