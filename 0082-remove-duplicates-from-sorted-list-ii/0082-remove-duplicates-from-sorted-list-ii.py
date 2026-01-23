# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        curr = head
        dummy_node = ListNode(0)
        start = dummy_node
        
        while curr.next:
            
            temp = curr.next
            
            if temp:
                if temp.val == curr.val:
                    while temp and temp.val == curr.val:
                        temp = temp.next
                else:
                    if not dummy_node.next:
                        dummy_node.next = curr
                        
                    start = curr


            start.next = temp
            if start.next:
                print(f"start = {start.val}, start points to {start.next.val}")
            else:
                print(f"start = {start.val}, start points to {start.next}")

            curr = start.next

            if curr == None:
                break

        return dummy_node.next