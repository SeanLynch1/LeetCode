class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        counter = Counter(nums)
        maj_element = nums[0]
        count = 0

        print(counter)
        for key, value in counter.items():
            print(key,value)
            if value > count:
                count = value
                maj_element = key
        
        return maj_element

