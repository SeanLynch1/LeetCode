class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        n = len(nums)

        if n == 0:
            return
            
        k = k % n

        def ref(x, y):

            while x < y:
                nums[y], nums[x] = nums[x], nums[y]

                x += 1
                y -= 1

        ref(0, n - 1)
        ref(0,k - 1)
        ref(k, n - 1)