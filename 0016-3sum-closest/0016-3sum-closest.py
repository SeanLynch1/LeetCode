class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        closest_sum = sum(nums[:3])
        closest_distance = abs(target - closest_sum)

        print("nums = ", nums)
        print("closest_sum = ", closest_sum)
        print("closest_distance = ", closest_distance)
        print("\n")

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                
                remaining = target - nums[i]

                print("j = ", j, "k = ", k)

                curr_sum = (nums[i] + nums[j] + nums[k])

                print(f"current sum of {nums[i]}, {nums[j]}, {nums[k]} = ", curr_sum)

                if abs(target - curr_sum) < closest_distance:
                    closest_distance = abs(target - curr_sum)
                    closest_sum = curr_sum

                    print("closest_sum = ", closest_sum)
                    print("closest distance = ", closest_distance, "\n")  

                if nums[j] + nums[k] < remaining: 
                    j += 1
                elif nums[j] + nums[k] > remaining:
                    k -= 1
                else:
                    return target

                



        return closest_sum    
