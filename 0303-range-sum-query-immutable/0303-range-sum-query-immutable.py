class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixes = [0]

        for i in range(1, len(nums) + 1):
            self.prefixes.append(sum(nums[:i]))
        
        print(self.prefixes)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixes[right + 1] - self.prefixes[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# 1 4 3 2 9  9  1  2 
# 0 1 5 8 10 19 28 29 31