class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        
        #strt  [-5,-2,3,5]
        #left  [0 , 3,5,2]
        #right [3 , 5,2,0]

        #left  [0, 1, 5,1]
        #right [1, 5, 1,0]

        #left  [7, 6,1, 0]
        #right [0,1, 6, 7]

        ans = []
        n = len(nums)
        left = [0] * n
        right = [0] * n

        for i in range(n):
            if i - 1 >= 0:
                left[i] = abs(nums[i] - nums[i-1])
            if i + 1 < n:
                right[i] = abs(nums[i] - nums[i+1])
            
        prefixes = [0]

        for i in range(0, n-1):
            if i == 0:
                prefixes.append(1)
            elif left[i] > right[i]:
                prefixes.append(prefixes[-1] + 1)
            else:
                prefixes.append(prefixes[-1] + right[i])

        suffixes = [0] * n

        for i in range(n-1,0,-1):
            if i == n-1:
                suffixes[i-1] = 1
            elif right[i] >= left[i]:
                suffixes[i-1] = suffixes[i] + 1
            else:
                suffixes[i-1] = suffixes[i] + left[i]

        for l, r in queries:
            total = 0
            # left to right
            if r > l:
                total = abs(prefixes[r] - prefixes[l])
            
            elif l > r:
                total = abs(suffixes[l] - suffixes[r])

            ans.append(total)

        return ans
