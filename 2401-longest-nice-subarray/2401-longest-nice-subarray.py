class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        longest = 0

        for i, ch in enumerate(nums):
            

            count = 1

            bit_start = nums[i]

            right = i + 1
            print(f"start word = {bit_start}")

            while right < len(nums) and nums[right] & bit_start == 0:
                
                print(f"word = {nums[right]}")
                print(f"binary of start word {bin(bit_start)}")
                print(f"binary of word = {bin(nums[right])}")

                bit_start |= nums[right]
                
                print(f"output = {bin(bit_start)}")
                count += 1
                right += 1

            longest = max(count, longest)

            print("")

        return longest