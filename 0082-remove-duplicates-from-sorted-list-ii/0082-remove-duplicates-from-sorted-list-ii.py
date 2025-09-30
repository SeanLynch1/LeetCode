# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode(-101)
        dummy.next = head

        curr = dummy
        temp = curr

        duplicated_val = dummy.val

        while temp.next:
            
            if temp.next.val == duplicated_val:
                temp = temp.next
            else:
                temp = temp.next

                if temp.next != None:
                    if temp.val != temp.next.val:
                        curr.next = temp
                        curr = curr.next
                else:
                    curr.next = temp
                    curr = curr.next


            duplicated_val = temp.val

        
        curr.next = temp.next


        return dummy.next
