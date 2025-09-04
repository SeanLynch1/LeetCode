class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # normaliize k 
        # k will represent the number of digits in each section that are shifted, it will be used as the "splitting point"
        # everything gets shifted, but it's really just two sections getting shifted

        n = len(nums)
        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]

                left += 1
                right -= 1
        
        reverse(0, n - 1)

        print(nums)

        # reverse left section
        reverse(0, k - 1)

        print(nums)
        # reverse right section
        reverse(k, n - 1)

        print(nums)

        return nums