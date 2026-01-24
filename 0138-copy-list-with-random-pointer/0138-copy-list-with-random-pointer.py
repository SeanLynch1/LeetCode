"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        mapping = {}
        curr = head
        dummy_node = Node(-101, None, None)
        copy = dummy_node

        while curr:
            if curr not in mapping:
                mapping[curr] = Node(curr.val)

            copy.next = mapping[curr]
            copy = copy.next

            if curr.random:
                if curr.random not in mapping:
                    mapping[curr.random] = Node(curr.random.val)

                copy.random = mapping[curr.random]

            if copy.random:
                print(copy.val, f"next = {copy.next}, ", f"random = {copy.random.val}")

            curr = curr.next

            print("\n")


        while head:
            if mapping[head].random:
                if mapping[head].next:
                    print(mapping[head].val, mapping[head].next.val, mapping[head].random.val)
                else:
                    print(mapping[head].val, mapping[head].next, mapping[head].random.val)
            else:
                if mapping[head].next:
                    print(mapping[head].val, mapping[head].next.val, mapping[head].random)
                else:
                    print(mapping[head].val, mapping[head].next, mapping[head].random)

            head = head.next

        return dummy_node.next