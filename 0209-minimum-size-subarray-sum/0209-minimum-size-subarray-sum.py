class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        output = 0
        start, end, left, right = 0, 0, 0, 0
        summation = 0

        while right < len(nums):
            

            summation += nums[right]
            print("before: ")
            print("left = ", left, ", right =", right)
            print("summation = ", summation, "target = ", target)
            while summation >= target:
                
                if right - left < end - start or end == 0:
                    print("hello")
                    start, end = left, right
                    output = end - start + 1
                    print(start, end, output)

                summation -= nums[left]
                left += 1
                print("left = ", left)
                print("summation = ", summation)

            right += 1

            print("\n")
        
        return output


