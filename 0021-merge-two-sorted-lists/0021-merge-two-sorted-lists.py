# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        curr_red = list1

        curr_purple = list2

        dummy_node = ListNode(0)
        curr = dummy_node

        while curr:
            if not curr_purple:
                curr.next = curr_red
                break
            elif not curr_red:
                curr.next = curr_purple
                break

            if curr_purple.val <= curr_red.val:
                curr.next = curr_purple
                curr_purple = curr_purple.next
            else:
                curr.next = curr_red
                curr_red = curr_red.next

            curr = curr.next


        return dummy_node.next