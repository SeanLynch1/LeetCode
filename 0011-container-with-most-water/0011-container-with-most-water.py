class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0

        left = 0
        right = len(height) - 1

        while left < right:

            left_height = height[left]
            right_height = height[right]

            max_water = max(max_water, min(left_height, right_height) * (right - left))

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_water