# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1

        k = count - (k % count) + 1

        curr = head

        new = ListNode()

        for i in range(1,k):
            if i+1 == k:
                new.next = curr.next
                curr.next = None
                break

            curr = curr.next

        temp = new

        while temp.next:
            temp = temp.next

        temp.next = head
        print(new)


        return new.next


             
        
