class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # less than or equal to target bring right forward one

        min_int = float('inf')
        left = 0
        right = 0
        
        curr = nums[left]
        temp = deque([nums[left]])
            
        while right < len(nums):
            
            if curr >= target:
                min_int = min(min_int, len(temp))
                curr -= nums[left]
                temp.popleft()
                left += 1
            else:
                right += 1
                if right < len(nums):
                    curr += nums[right]
                    temp.append(nums[right])

        return min_int if min_int != float('inf') else 0

            
