class Node:

    def __init__(self, start, end, idx):
        self.start = start
        self.end = end
        self.idx = idx
        self.next = None

class Solution:

    def __init__(self, w: List[int]):
        self.curr = Node(1, w[0], 0)
        start = self.curr

        self.sum = w[0]

        for i in range(1, len(w)):
            interval = w[i]
            s = self.sum + 1
            e = self.sum + interval
            self.sum += interval
            
            self.curr.next = Node(s, e, i)
            self.curr = self.curr.next

        self.curr = start

        s = self.curr

    def pickIndex(self) -> int:
        curr = self.curr
        random_no = random.randrange(1,self.sum + 1)
        while curr:
            
            if curr.start <= random_no and curr.end >= random_no:
                return curr.idx

            curr = curr.next




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()