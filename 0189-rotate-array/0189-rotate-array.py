class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def gcd(a, b) -> int:

            if b == 0:
                return a

            return gcd(b, a % b)

        cycles = gcd(n, k)

        for c in range(cycles):
            last = nums[c]
            jump = c

            while True:
                jump += k
                jump %= n

                curr = nums[jump]
                nums[jump] = last
                last = curr
                
                if jump == c:
                    break