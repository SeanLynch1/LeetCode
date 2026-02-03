class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        left = k
        right = n - k - 1

        slic = nums[right + 1:]

        while right >= 0:

            nums[right + k] = nums[right]
            right -= 1

        for i in range(k):
            nums[i] = slic[i]


