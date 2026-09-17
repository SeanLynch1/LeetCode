class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        # window sum
        # [1, 2, 3] = 6

        # end sums
        # [1] = 1
        # [1,2] [2] = 6
        # [1,2,3] [2,3] [3] = 20

        # final 
        # [1] = 1
        # [1,2] [2] = 6
        # [2,3] [3] = 14


        # window sum
        # [2, 3, 5] = 10

        # end sums
        # [1] = 1
        # [1,2] [2] = 6
        # [2,3] [3] = 14
        # [2, 3, 5] [3, 5] [5] = 37

        # final 
        # [1] = 1
        # [1,2] [2] = 6
        # [2,3] [3] = 14
        # [5] = 19

        def count_sums(k: int) -> list:
            window_sum = 0
            ending_sum = 0

            left_pointer = 0
            total = 0
            count = 0

            for right_pointer in range(len(nums)):
                num = nums[right_pointer]

                window_sum += num
                ending_sum += num * (right_pointer - left_pointer + 1)

                while window_sum > k:
                    ending_sum -= window_sum
                    window_sum -= nums[left_pointer]
                    left_pointer += 1

                total += ending_sum
                count += (right_pointer - left_pointer + 1)

            return [count, total]

        def find_optimal(k: int) -> int:
            if k == 0:
                return 0

            low = min(nums)
            high = sum(nums)

            while high > low:

                mid = (low + high) // 2
                count, total = count_sums(mid)

                if count >= k:
                    high = mid
                else:
                    low = mid + 1

            count, total = count_sums(low)

            diff = count - k
            total -= (low * diff)
            # 1,2,3,3,4,5,6,7,9,10
            
            return total

        return (find_optimal(right) - find_optimal(left - 1)) % ((10 ** 9) + 7)