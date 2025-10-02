class DoublyNode:
    def __init__(self, val, key):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes_in_list = 0
        self.lru = DoublyNode(-1, -1)
        self.mru = DoublyNode(-1, -1)
        self.lru.next = self.mru
        self.mru.prev = self.lru
        self.hash = {}

    def get(self, key: int) -> int:
        if key in self.hash:
            self.remove(self.hash[key])
            self.append(self.hash[key])
            return self.hash[key].val

        return -1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def append(self, node):
        node.next = self.mru
        node.prev = self.mru.prev
        self.mru.prev.next = node
        self.mru.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])
            self.append(self.hash[key])
            self.hash[key].val = value
        else:
            self.nodes_in_list += 1
            if self.nodes_in_list > self.capacity:
                self.nodes_in_list -= 1
                del self.hash[self.lru.next.key]
                self.remove(self.lru.next)
            node = DoublyNode(value, key)
            self.hash[key] = node
            self.append(node)