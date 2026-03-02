class Solution:

    def __init__(self, w: List[int]):
        
        self.prefixes = [0]
        self.sum = 0

        for val in w:
            self.prefixes.append(self.sum + val)
            self.sum += val

    def pickIndex(self) -> int:

        random_no = random.randrange(0, self.sum)

        idx = bisect_right(self.prefixes, random_no)
        return idx - 1
        




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()