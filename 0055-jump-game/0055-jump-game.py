class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = 0
        while i < len(nums) - 1:
            print("i = ", i)
            if nums[i] == 0:
                return False
            
            target = nums[i] + i

            print("target = ", target)

            for j in range(i + 1, i + nums[i] + 1):
                print("j = ", j)

                if j >= len(nums) - 1:
                    return True
                elif nums[j] + j >= target:
                    target = nums[j] + j
                    i = j

                    print("i = ", j, "target = ", nums[j])

                print("\n")

        return True
