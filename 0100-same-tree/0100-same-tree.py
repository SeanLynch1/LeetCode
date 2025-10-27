# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterative solution
        stack = [(p, q)]

        while stack:
            curr_p, curr_q = stack.pop()

            if not curr_p and not curr_q:
                continue
            elif curr_p and not curr_q:
                return False
            elif curr_q and not curr_p:
                return False
            elif curr_p.val != curr_q.val:
                return False

            stack.append((curr_p.left, curr_q.left))
            stack.append((curr_p.right, curr_q.right))

        return True

        # my iterative solution
        '''stack = []
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

        return True'''

            
