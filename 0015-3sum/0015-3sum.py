class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()

        for i in range(len(nums)):

            target = nums[i] 
            left = i + 1
            right = len(nums) - 1
            
            if i > 0 and target == nums[i - 1]:
                continue

            while left < right:
                
                curr_left = nums[left]
                curr_right = nums[right]
                two_sum = curr_right + curr_left

                if target + two_sum == 0:
                    output.append([target, curr_left, curr_right])
                

                if target + two_sum >= 0:
                    right -= 1
                else:
                    left += 1

                

        return output