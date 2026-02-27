class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.rle = deque()

        for i in range(1, len(encoding), 2):
            if encoding[i - 1] > 0:
                self.rle.append([encoding[i], encoding[i-1]])

        self.curr = self.rle.popleft()

        print(self.rle)
        print("")

    def next(self, n: int) -> int:
        
        if not self.curr:
            return -1

        res = self.curr[0]

        total = n
        print(self.curr, f"total = {total}")

        while total > 0:
            num_count = self.curr[1]

            if num_count - total < 0:
                total -= num_count
                if self.rle:
                    self.curr = self.rle.popleft()
                    res = self.curr[0]
                    print(f"popping, self.curr = {self.curr}")
                else:
                    return -1
            elif num_count - total == 0:
                print(f"{num_count} - {total} == 0")
                if self.rle:
                    self.curr = self.rle.popleft()
                else:
                    return -1

                return res
            else:
                self.curr[1] -= total
                print(self.curr, f"total = {self.curr[1]}")

                break
        print("")
        return res


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)