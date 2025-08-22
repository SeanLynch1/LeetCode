class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = sum(nums[:3])  # initial guess

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]

                # update best
                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum

                if curr_sum < target:
                    j += 1
                elif curr_sum > target:
                    k -= 1
                else:  # exact match
                    return target

        return closest_sum
