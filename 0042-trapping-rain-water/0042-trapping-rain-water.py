class Solution:
    def trap(self, height: List[int]) -> int:
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
                if left_peak < height[left]:
                    left_peak = height[left]

                diff = left_peak - height[left + 1]

                if diff > 0:
                    water_bucket += diff
                else:
                    water += water_bucket
                    water_bucket = 0
                left += 1
            else:

                if right_peak < height[right]:
                    right_peak = height[right]

                diff = right_peak - height[right - 1]
                if diff > 0:
                    water_bucket += diff
                else:
                    water += water_bucket
                    water_bucket = 0
                right -= 1


        return water