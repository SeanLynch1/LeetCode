# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0 or not head.next:
            return head

        curr = head
        count = 1

        while curr.next:
            curr = curr.next
            count += 1

        k = count - (k % count)

        if k == count:
            return head
            
        print("count = ", count)
        print(k % count)
        temp = head
        print("k = ", k)
        for i in range(1, k):
            temp = temp.next

        print("curr = ", curr)
        print(temp)

        start = temp.next
        temp.next = None
        print(head)
        curr.next = head

        return start


             
        
