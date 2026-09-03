class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # [1,2,3,2,3,4 ,1 ,2 ]

        # [0,1,3,6,8,11,15,16,18]

        mapping = defaultdict(int)
        mapping[0] = 1
        prefixes = [0] * (len(nums) + 1)
        output = 0
        last = 0
        for i in range(len(nums)):
            val = last + nums[i]
            prefixes[i + 1] = val
            last = val
            
            output += mapping[val - k]
            mapping[val] += 1


        return output