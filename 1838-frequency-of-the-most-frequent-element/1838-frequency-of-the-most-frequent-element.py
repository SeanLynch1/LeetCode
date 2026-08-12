class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        

        nums.sort()
        output = 1
        prefixes = [0]
        diff = 0

        for num in nums:
            prefixes.append(prefixes[-1] + num)

        print(prefixes)

        # k = 5
        # [1, 2, 4, 5, 7]
        # [0, 1, 3, 7, 12, 19]

        curr = 0
        # sliding window
        for i in range(len(nums)):
            target = nums[i]
            diff = 0
            nxt = i
            
            for j in range(curr, nxt):
                needed = (i - j + 1) * target
                total = prefixes[nxt + 1] - prefixes[j]
                diff = needed - total

                if diff <= k:
                    output = max(output, i + 1 - j)
                    curr = j
                    break

        return output