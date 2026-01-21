# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack = [p, q]

        while stack:
            
            curr_q = stack.pop()
            curr_p = stack.pop()

            if not curr_q and not curr_p:
                continue

            if not curr_q or not curr_p:
                return False

            if curr_q.val != curr_p.val:
                return False

            stack.append(curr_p.left)
            stack.append(curr_q.left)

            stack.append(curr_p.right)
            stack.append(curr_q.right)

        return True
