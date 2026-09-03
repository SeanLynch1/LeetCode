class ProductOfNumbers:

    def __init__(self):
        self.zeroes = [0]
        self.prefixes = [1]
        self.list = []

    def add(self, num: int) -> None:
        self.list.append(num)

        if num == 0:
            self.zeroes.append(self.zeroes[-1] + 1)
            self.prefixes.append(self.prefixes[-1] * 1)
        else:
            self.zeroes.append(self.zeroes[-1])
            self.prefixes.append(self.prefixes[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.zeroes[-1] - self.zeroes[len(self.zeroes) - k - 1] > 0:
            return 0
        return int(self.prefixes[-1] / self.prefixes[(len(self.prefixes) - k - 1)])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)