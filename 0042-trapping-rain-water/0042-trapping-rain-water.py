class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        water = 0

        l_height = height[left]
        r_height = height[right]

        while left < right:
            if height[left] < height[right]:
                
                if height[left] > l_height:
                    l_height = height[left]
                else:
                    water += l_height - height[left]

                left += 1
            else:
                if height[right] > r_height:
                    r_height = height[right]
                else:
                    water += r_height - height[right]
                right -= 1

        return water