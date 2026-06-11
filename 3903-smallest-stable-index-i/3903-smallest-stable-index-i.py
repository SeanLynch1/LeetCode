class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        # k = 3
        # [0, 2, 3, 1, 4, 2, 5]

        # left = max[0] = 0 - right = min[0,2,3,1,4,2,5]
        # left = max[0,2] = 2 - right = min[]

        prefixes = []
        curr = nums[0]

        for n in nums:
            val = max(n,curr)
            prefixes.append(val)
            curr = val

        print(prefixes)

        suffixes = [0] * len(nums)
        curr = float('inf')
        
        for i in range(len(nums)-1,-1,-1):
            val = min(nums[i],curr)
            suffixes[i] = val
            curr = val

        print(suffixes)

        for i in range(len(nums)):
            left = prefixes[i]
            right = suffixes[i]

            print(f"{left} - {right}")
            if left - right <= k:
                return i

            print("")
        return -1