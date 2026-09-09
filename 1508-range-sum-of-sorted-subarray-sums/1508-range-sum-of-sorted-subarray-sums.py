from typing import List

class Solution:
    def rangeSum(
        self,
        nums: List[int],
        n: int,
        left: int,
        right: int
    ) -> int:

        MOD = 10**9 + 7

        # Returns:
        # 1. Number of subarray sums <= target
        # 2. Total of all subarray sums <= target
        def count_and_sum(target):
            count = 0
            total = 0

            window_sum = 0
            ending_sum = 0
            left_pointer = 0

            for right_pointer, num in enumerate(nums):
                window_sum += num

                # Add num to every valid subarray ending
                # at right_pointer, plus the new [num] subarray.
                ending_sum += num * (right_pointer - left_pointer + 1)

                # nums contains only positive values.
                # Shrink until window_sum <= target.
                while window_sum > target:
                    # Remove the subarray:
                    # nums[left_pointer:right_pointer + 1]
                    ending_sum -= window_sum
                    window_sum -= nums[left_pointer]
                    left_pointer += 1

                number_of_subarrays = right_pointer - left_pointer + 1

                count += number_of_subarrays
                total += ending_sum

            return count, total

        # Returns the sum of the k smallest subarray sums.
        def sum_first_k(k):
            if k == 0:
                return 0

            low = min(nums)
            high = sum(nums)

            # Find the smallest value such that at least
            # k subarray sums are <= that value.
            while low < high:
                mid = (low + high) // 2
                count, _ = count_and_sum(mid)

                if count >= k:
                    high = mid
                else:
                    low = mid + 1

            threshold = low
            count, total = count_and_sum(threshold)

            # count may be greater than k because multiple
            # subarrays can have the same sum as threshold.
            total -= (count - k) * threshold

            return total

        return (
            sum_first_k(right) -
            sum_first_k(left - 1)
        ) % MOD