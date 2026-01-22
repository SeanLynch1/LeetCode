class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.last = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = {}
        self.tail = Node(0,0)
        self.head = Node(0,0)

        self.head.last = self.tail
        self.tail.next = self.head

        self.capacity = capacity


    def remove(self, node: Node) -> None:
        node.next.last = node.last
        node.last.next = node.next

    def add_node(self, node: Node) -> Node:
        last_node = self.head.last  

        node.next = self.head
        node.last = last_node

        self.head.last = node
        last_node.next = node

        return node

    def get(self, key: int) -> int:

        if key in self.mapping:
            # rearrange head
            node = self.mapping[key]

            self.remove(node)
            val = self.add_node(node).val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.mapping:
            # update key
            node = self.mapping[key]
            
            self.remove(node)
            node = self.add_node(node)
            node.val = value
        else:
            # remove first node
            if len(self.mapping) == self.capacity:
                
                first_node = self.tail.next

                self.remove(first_node)
                del self.mapping[first_node.key]

            
            # add new node
            self.mapping[key] = Node(key, value)
            self.add_node(self.mapping[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)