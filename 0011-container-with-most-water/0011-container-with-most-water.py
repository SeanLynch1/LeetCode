class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        heighest_pillar = 0


        while left < right: 
            lower_value = min(height[left], height[right])

            if lower_value > heighest_pillar:
                current_area = lower_value * (right - left)

                if current_area > max_area:
                    max_area = current_area

                heighest_pillar = lower_value

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area