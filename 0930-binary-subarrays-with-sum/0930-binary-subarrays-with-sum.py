class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        #  1 0 1 0 1
        # [0 1 1 2 2 3]

        total = 0
        mapping = defaultdict(int)
        mapping[0] = 1

        prefix = [0]

        for num in nums:

            val = prefix[-1] + num
            prefix.append(val)
            needed = val - goal

            if needed in mapping:
                total += mapping[needed]

            mapping[val] += 1

        return total