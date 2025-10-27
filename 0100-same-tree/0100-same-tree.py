# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack = []
        curr_p = p
        curr_q = q

        while stack or curr_p or curr_q:
            while curr_p or curr_q:

                if not (curr_p and curr_q) or curr_p.val != curr_q.val:
                    return False
                
                stack.append(curr_p)
                stack.append(curr_q)

                curr_p = curr_p.left
                curr_q = curr_q.left

            curr_q = stack.pop().right
            curr_p = stack.pop().right



        return True

            
