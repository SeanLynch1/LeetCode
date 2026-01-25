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

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1


                

        return output