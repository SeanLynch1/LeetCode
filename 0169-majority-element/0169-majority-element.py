class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        counter = Counter(nums)
        maj_element = nums[0]
        count = 0

        for key, value in counter.items():
            if value > count:
                count = value
                maj_element = key
        
        return maj_element

