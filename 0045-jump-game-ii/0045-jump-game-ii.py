class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        i = 0
        jumps = 1

        while i < len(nums) - 1:
            
            current_jump = i + nums[i] + 1

            if current_jump >= len(nums):
                break
            
            for j in range(i, current_jump):
                print("j = ", j)
                if nums[j] + j > current_jump - 1:
                    current_jump = nums[j] + j + 1
                    i = j
                    
            jumps += 1
            print("Jumps = ", jumps)
            print("jumping to index : ", i)
            print("\n")

        print("jumps = ", jumps)
        return jumps

