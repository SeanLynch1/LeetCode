class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        stack = []
        prefix = [0]
        ans = 0

        for num in nums:
            prefix.append(prefix[-1] + num)

        for i in range(len(nums)):
            num = nums[i]
            new_start = i

            while stack and stack[-1][1] > num:
                start, val = stack.pop()
                total = prefix[i] - prefix[start]

                ans = max(ans, total * val)
                new_start = start

            stack.append([new_start, num])

        for start, val in stack:
            ans = max(val * (prefix[len(prefix)-1] - prefix[start]), ans)

        return ans % (10 ** 9 + 7)