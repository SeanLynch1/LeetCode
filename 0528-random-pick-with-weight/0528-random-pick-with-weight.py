class Solution:

    def __init__(self, w: List[int]):
        
        self.prefixes = [0]
        self.sum = 0

        for val in w:
            self.prefixes.append(self.sum + val)
            self.sum += val

        print(self.prefixes)
        print(self.sum)

    def pickIndex(self) -> int:

        random_no = random.randrange(0, self.sum)

        print(f"random_no = {random_no}")
        idx = bisect_right(self.prefixes, random_no)
        print(f"idx = {idx}")
        return idx - 1
        




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()