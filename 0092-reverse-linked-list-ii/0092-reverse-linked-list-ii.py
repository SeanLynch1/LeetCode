# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head, label="List"):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(f"{label}: {arr}")

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            print("No operation needed.")
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        print_list(dummy.next, "Initial")

        # Step 1: Move prev to node before `left`
        for i in range(left - 1):
            prev = prev.next
            print(f"prev = {prev}")

        # start = start of reverse
        start = prev.next

        # 1 after start of reverse
        then = start.next
        print(f"Start = {start}, ")
        print(f"Then ={then}")

        # Step 2: Reverse nodes between left and right
        for i in range(right - left):
            print(f"\nIteration {i+1}:")
            start.next = then.next
            print("start = ",start)
            then.next = prev.next
            print("then = ",then)
            prev.next = then
            print("prev = ", prev)

            #print_list(dummy.next, "  Current list")

            then = start.next
            print("then = ", then)

            print("\n")

        print_list(dummy.next, "Final")
        return dummy.next

