class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        water = 0
        water_bucket = 0
        left = 0
        right = len(height) - 1
        left_peak = height[left]
        right_peak = height[right]

        # loop both directions
        while right > left:
            # find lowest side
            if height[left] < height[right]:

                left += 1

                if left_peak < height[left]:
                    left_peak = height[left]

                diff = left_peak - height[left]
                water += diff

            else:
                right -= 1

                if right_peak < height[right]:
                    right_peak = height[right]

                diff = right_peak - height[right]
                water += diff


        return water