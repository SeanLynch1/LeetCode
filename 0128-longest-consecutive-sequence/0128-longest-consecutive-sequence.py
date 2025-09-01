class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                length = 1
                nxt = current_num + 1

                while nxt in nums_set:
                    length += 1
                    nxt += 1

                max_len = max(length,max_len)

        
        return max_len