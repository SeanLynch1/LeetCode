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


    def get_node(self, key: int) -> Node:
        node = self.mapping[key]
        last_node = self.head.last  

        if node == last_node:
            return node

        node.next.last = node.last
        node.last.next = node.next

        node.next = self.head
        node.last = last_node

        last_node.next.last = node
        last_node.next = node

        return node

    def add_node(self, key: int) -> None:
        node = self.mapping[key]
        last_node = self.head.last  

        node.next = self.head
        node.last = last_node

        last_node.next = node
        node.next.last = node

    def get(self, key: int) -> int:

        if key in self.mapping:
            # rearrange head
            val = self.get_node(key).val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.mapping:
            # update key


            node = self.get_node(key)
            node.val = value
        else:

            # remove first node
            if len(self.mapping) == self.capacity:
                
                first_node = self.tail.next

                del self.mapping[first_node.key]

                first_node.next.last = self.tail

                self.tail.next = first_node.next
            
            # add new node
            self.mapping[key] = Node(key, value)
            self.add_node(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)