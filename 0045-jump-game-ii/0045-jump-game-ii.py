class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        i = 0
        jumps = 0

        while i < len(nums) - 1:
            
            if i >= len(nums):
                break

            cap = min(i + nums[i] + 1, len(nums))

            best = 0
            print("cap = ", cap - 1)

            if cap >= len(nums):
                jumps += 1
                break
            
            print("best = ", best)
            for j in range(i, cap):
                if nums[j] + j > best:
                    best = nums[j] + j
                    i = j
                    
            jumps += 1

            print("best = ", best, "jumping to index : ", i)

            print("\n")
    
        return jumps

