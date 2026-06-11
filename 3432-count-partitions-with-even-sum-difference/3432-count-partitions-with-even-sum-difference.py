class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        # [1, 2, 5, 3, 2,  1,  4]  ##
        # [0, 1, 3, 8, 11, 13, 14, 18]

        # left = [0, 0], right = [1, 6]
        # left = [0, 1], right = [2, 6]
        # left = [0, 2], right = [3, 6]
        # left = [0, 3], right = [4, 6]
        # left = [0, 4], right = [5, 6]
        # left = [0, 5], right = [6, 6]
        ans = 0
        prefixes = [0]
        for n in nums:
            prefixes.append(prefixes[-1] + n)

        for i in range(len(nums)-1):
            left_sum = prefixes[i + 1]
            right_sum = prefixes[len(nums)] - prefixes[i+1]
                
            print(f"{left_sum} - {right_sum} = {left_sum - right_sum}")

            if (left_sum - right_sum) % 2 == 0:
                print(f"{(left_sum - right_sum) % 2 }")
                ans += 1
            print("")
        return ans