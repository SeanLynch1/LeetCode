class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        # [1, 2, 4, 3, 5, 1]
        # [1, 2, 4]
        
        output_max = 0
        output_min = 0
        stack_min = []
        stack_max = []

        # find total for mins
        for i, num in enumerate(nums):
            
            # increasing monotonic stack
            while stack_min and num < stack_min[-1][1]:
                
                j, popped_val = stack_min.pop()

                # count left side
                left = j - stack_min[-1][0] if stack_min else j + 1

                # count right side
                right = i - j
                # math trick to find total subarrays using left and right
                output_min = (output_min + right * left * popped_val)

            stack_min.append([i, num])

            # decreasing monotonic stack
            while stack_max and num > stack_max[-1][1]:
                
                j, popped_val = stack_max.pop()

                # count left side
                left = j - stack_max[-1][0] if stack_max else j + 1

                # count right side
                right = i - j
                # math trick to find total subarrays using left and right
                output_max = (output_max + right * left * popped_val)
                
            stack_max.append([i, num])

        for i in range(len(stack_min)):
            idx, num = stack_min[i]

            left = idx - stack_min[i-1][0] if i > 0 else idx + 1

            right = len(nums) - idx

            output_min = (output_min + right * left * num)

        for i in range(len(stack_max)):
            idx, num = stack_max[i]

            left = idx - stack_max[i-1][0] if i > 0 else idx + 1

            right = len(nums) - idx

            output_max = (output_max + right * left * num)

        return output_max - output_min