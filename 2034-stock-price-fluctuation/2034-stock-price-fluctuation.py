import heapq

class StockPrice:

    def __init__(self):
        self.stocks = defaultdict(int)
        self.min_prices = []
        self.max_prices = []
        self.max_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        if price == self.stocks[timestamp]:
            return

        self.stocks[timestamp] = price
        self.max_timestamp = max(timestamp, self.max_timestamp)

        # min prices
        heapq.heappush(self.min_prices, (price, timestamp))

        # max prices
        heapq.heappush(self.max_prices, (price * -1, timestamp))

    def current(self) -> int:
        return self.stocks[self.max_timestamp]

    def maximum(self) -> int:
        
        max_val = abs(self.max_prices[0][0])

        while max_val != self.stocks[self.max_prices[0][1]]:

            heapq.heappop(self.max_prices)
            max_val = abs(self.max_prices[0][0])
        
        return max_val
    def minimum(self) -> int:
        
        min_val = self.min_prices[0][0]

        while min_val != self.stocks[self.min_prices[0][1]]:

            heapq.heappop(self.min_prices)
            min_val = self.min_prices[0][0]
        
        return min_val
