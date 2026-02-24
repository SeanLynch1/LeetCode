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
                s = nums[left] + nums[right] + target
                if s == 0:
                    output.append([target,  nums[left], nums[right]])
                    left += 1
                    right -=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif s >= 0:
                    right -= 1
                else:
                    left += 1
            

        return output