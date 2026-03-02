import heapq
from collections import defaultdict

class StockPrice:

    def __init__(self):
        self.stocks = defaultdict(int)
        self.min_prices = []
        self.max_prices = []
        self.max_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        
        self.stocks[timestamp] = price
        self.max_timestamp = max(self.max_timestamp, timestamp)

        # push into both heaps
        heapq.heappush(self.min_prices, (price, timestamp))
        heapq.heappush(self.max_prices, (-price, timestamp))

    def current(self) -> int:
        return self.stocks[self.max_timestamp]

    def maximum(self) -> int:

        # lazy delete stale max entries
        while True:
            neg_price, ts = self.max_prices[0]
            price = -neg_price
            if self.stocks[ts] == price:
                return price
            heapq.heappop(self.max_prices)

    def minimum(self) -> int:

        # lazy delete stale min entries
        while True:
            price, ts = self.min_prices[0]
            if self.stocks[ts] == price:
                return price
            heapq.heappop(self.min_prices)