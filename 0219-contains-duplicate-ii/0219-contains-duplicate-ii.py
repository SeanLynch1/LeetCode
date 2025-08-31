class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set()
        j = 0

        for i in range(len(nums)):
            
            while len(window) <= k:
                
                if j >= len(nums):
                    return False

                if nums[j] in window:
                    return True

                window.add(nums[j])
                
                j += 1

            

            window.remove(nums[i])

        return False