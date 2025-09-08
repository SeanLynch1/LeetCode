class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        bucket = 0
        water = 0

        l_height = height[left]
        r_height = height[right]

        while left < right:
            if height[left] < height[right]:
                
                if height[left] > l_height:
                    water += bucket
                    l_height = height[left]
                    bucket = 0
                else:
                    bucket += l_height - height[left]

                left += 1
            else:
                if height[right] > r_height:
                    water += bucket
                    r_height = height[right]
                    bucket = 0
                else:
                    bucket += r_height - height[right]
                right -= 1

        return water + bucket