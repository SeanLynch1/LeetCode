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

        temp = self.head


    def remove(self, key: int):
        print(f"removing key, {key}")
        prev, next = self.my_dict[key].prev, self.my_dict[key].next
        prev.next = next
        next.prev = prev

        del self.my_dict[key]
        
        

    def insert(self, key: int):
        prev, next = self.head, self.head.next

        print(f"inserting {key}")
        
        next.prev = self.my_dict[key]
        self.head.next = self.my_dict[key]

        self.my_dict[key].prev = prev
        self.my_dict[key].next = next
        

    def get(self, key: int) -> int:
        
        print(f"getting key, {key}")
        if key not in self.my_dict:

            print(f"key, {key} not in self.my_dict")
            print("\n")
            return -1
        else:
            value = self.my_dict[key].val
            self.remove(key)

            self.my_dict[key] = ListNode(key, value)
            self.insert(key)

            temp = self.head.next

            print("linked list = ")
            while temp.next:
                print(f"key = {temp.key}, val = {temp.val}, prev = {temp.prev.key}, next = {temp.next.key}")
                temp = temp.next

            print()
            print("dictionary status = ")
            for key, value in self.my_dict.items():
                print(f"key = {key}, val = {value.val}")
            
            print("\n")

            return self.my_dict[key].val

        

    def put(self, key: int, value: int) -> None:

        if key not in self.my_dict:
            self.my_dict[key] = ListNode(key, value)
            self.insert(key)

            if len(self.my_dict) > self.capacity:
                self.remove(self.tail.prev.key)
        else:
            self.remove(key)
            self.my_dict[key] = ListNode(key, value)
            self.insert(key)

        temp = self.head.next

        print("linked list = ")
        while temp.next:
            print(f"key = {temp.key}, val = {temp.val}, prev = {temp.prev.key}, next = {temp.next.key}")
            temp = temp.next

        print()
        print("dictionary status = ")
        for key, value in self.my_dict.items():
            print(f"key = {key}, val = {value.val}")
        
        print("\n")
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)