# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack_p, stack_q = [], []

        while stack_p or stack_q or p or q:
            
            # loop through lefts
            while p or q:
                if p and q:
                    if p.val != q.val:
                        return False
                else:
                    return False

                stack_p.append(p)
                stack_q.append(q)

                p = p.left
                q = q.left

            # hit None
            p = stack_p.pop()
            q = stack_q.pop()

            p = p.right
            q = q.right

        return True

        