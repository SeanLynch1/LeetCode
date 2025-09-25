# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        linked_list = {}
        curr = head
        idx = 1

        while curr:
            linked_list[idx] = curr
            temp_next = curr.next

            if idx == right:
                curr.next = linked_list[idx -1]
                if (left - 1) in linked_list:
                    linked_list[left - 1].next = curr
                else:
                    head = curr
            elif idx == left:
                curr.next = None
            elif idx > left and idx < right:
                print(f"setting {curr.next} to {linked_list[idx]}, idx = {idx}")
                curr.next = linked_list[idx - 1]
            elif idx == right + 1:
                linked_list[left].next = curr
            
            curr = temp_next
            idx += 1

        return head