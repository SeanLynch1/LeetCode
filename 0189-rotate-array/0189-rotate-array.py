class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # gcd implementation
        '''n = len(nums)

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
                    break'''

        
        # reverse implementation
        n = len(nums)
        left = 0
        right = n-1

        k = k % n

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right -=1

        left = 0
        right = k-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right -=1

        left = k
        right = n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right -=1
