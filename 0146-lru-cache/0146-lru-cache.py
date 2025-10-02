class ListNode:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.my_dict = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: ListNode):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

        
    def insert(self, node: ListNode):
        prev, next = self.head, self.head.next

        next.prev = node
        self.head.next = node

        node.prev = prev
        node.next = next

    def get(self, key: int) -> int:
        
        if key not in self.my_dict:
            return -1
        else:
            node = self.my_dict[key]

            self.remove(node)

            self.insert(node)

            return node.val

    def put(self, key: int, value: int) -> None:

        if key not in self.my_dict:
            node = ListNode(key, value)
            self.my_dict[key] = node
            self.insert(node)

            if len(self.my_dict) > self.capacity:
                node = self.tail.prev
                self.remove(node)
                del self.my_dict[node.key]

        else:
            node = self.my_dict[key]
            node.val = value
            self.remove(node)
            self.insert(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)