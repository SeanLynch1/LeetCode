class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # k = 2
        #[1,0,0,1,1]

        # sum <= 2
        # 1
        # 10, 0
        # 100, 00, 0
        # 1001,001,01,1
        # 0011,011,11,1

        # sum <= 1
        # 1
        # 10, 0
        # 100, 00, 0
        # 001, 01, 1
        # 011, 11, 1

        def atMost(k:int):
            if k == -1:
                return 0

            total = 0
            curr = 0
            left = 0

            for right in range(len(nums)):
                curr += nums[right]
                print(f"curr = {curr}, k = {k}")
                while curr > k:
                    curr -= nums[left]
                    left += 1
                    print(f"left = {left}")

                total += right - left + 1
                print("")
            return total

        return atMost(goal) - atMost (goal - 1)