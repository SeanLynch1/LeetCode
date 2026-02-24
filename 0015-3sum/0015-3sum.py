class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        n = len(nums)
        for start in range(n):
            


            if start > 0 and nums[start] == nums[start - 1]:
                continue

            target = nums[start]
            left = start + 1
            right = n - 1
            
            while right > left:
                
                if nums[left] + nums[right] + target == 0:
                    res = [target,  nums[left], nums[right]]

                    output.append(res)
                    left += 1
                    right -=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right] + 1:
                        right -= 1

                elif nums[left] + nums[right] + target >= 0:
                    right -= 1
                else:
                    left += 1
            

        return output