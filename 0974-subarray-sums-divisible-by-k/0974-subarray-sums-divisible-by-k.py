class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        # [4,5,0,-2,-3,1]
        # [0,4,9, 9, 7,4,5]
        # 5 - 0 = [4,5,0,-2,-3,1]
        # 4 - 9 = [-2,-3]
        # 4 - 9 = [0,-2,-3]
        # 4 - 4 = [5,0,-2,-3]
        # 9 - 9 = [0]
        # 9 - 4 = [5,0]
        # 9 - 4 = [5]

        res = 0
        prefix = [0]
        mapping = defaultdict(int)
        mapping[0] += 1

        for i, num in enumerate(nums):
            val = prefix[-1] + num
            prefix.append(val)  

            remainder = val % k

            if remainder in mapping:
                res += mapping[remainder]

            mapping[remainder] += 1

        
        return res