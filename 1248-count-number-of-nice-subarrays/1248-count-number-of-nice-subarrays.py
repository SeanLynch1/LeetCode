class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        counter = defaultdict(int)

        prefix = 0
        res = 0
        counter[0] = 1

        for num in nums:
            prefix += num % 2
            res += counter[prefix - k]
            counter[prefix] += 1

        return res