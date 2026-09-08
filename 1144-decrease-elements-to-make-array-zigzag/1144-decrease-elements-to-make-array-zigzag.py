class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
        n = len(nums)
        org = nums.copy()
        output = 0

        # go for evens
        for i in range(0,n-1):
            curr = nums[i]
            right = nums[i + 1]

            if i % 2 == 0:
                if right >= curr:
                    diff = (right - curr) + 1
                    nums[i+1] -= diff    
                    output += diff
            else:
                if right <= curr:
                    diff = (curr - right) + 1
                    nums[i] -= diff
                    output += diff  

        nums = org
        temp = 0

        # go for odds
        for i in range(0,n-1):
            curr = nums[i]
            right = nums[i + 1]

            if i % 2 == 0:
                if right <= curr:
                    diff = (curr - right) + 1
                    nums[i] -= diff    
                    temp += diff
            else:
                if right >= curr:
                    diff = (right - curr) + 1
                    nums[i+1] -= diff
                    temp += diff  

        return min(temp,output)