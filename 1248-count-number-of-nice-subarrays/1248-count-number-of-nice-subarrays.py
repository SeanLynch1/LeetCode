class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        # [2,2,2,1,2,2,1,2,2,2]
        # [0,0,0,0,1,1,1,2,2,2,2]

        counter = defaultdict(int)
        counter[0] = 1
        prefix = 0
        res = 0

        for num in nums:
            prefix += num % 2 

            res += counter[prefix - k]
            
            counter[prefix] += 1
        return res