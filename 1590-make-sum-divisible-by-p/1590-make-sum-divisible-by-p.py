class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        if not nums:
            return 0

        total = sum(nums)
        print(f"total = {total}")
        divisor = total % p #17
        if total % p == 0:
            return 0

        print("")
        print(f"divisor = {divisor}")

        curr = 0
        output = float('inf')
        prefixes = defaultdict(list)
        prefixes[0] = [-1,0]

        for i in range(len(nums)):
            num = nums[i]

            curr += num
            needed = (curr - divisor) % p
            
            if needed in prefixes:
                print(f"Found!! num = {num}, needed = {needed}")
                idx, curr_left = prefixes[needed]
                window = curr - curr_left

                print(f"idx = {idx}, curr_left = {curr_left}, curr = {curr}, window = {window}")

                if (total - window) % p == 0 and window != total:
                    output = min(output, i - prefixes[needed][0])

            prefixes[curr % p] = [i, curr]

        if output != float('inf'):
            return output
            
        return -1

        # [3,6,8,1], d = 2
        # 1 : 3, 9, 17
        # 2 : 18

        
        # [6, 2, 5, 2]
        # p = 8

        # total = 15

        # [6 % 9] = 6
        # [3 % 9] = 3 [9 % 9] = 0
        # [5 % 9] = 5 [8 % 9] = 8 [14 % 9] = 5
        # [2 % 9] = 2 [7 % 9] = 7 [10 % 9] = 1 [16 % 9] = 7