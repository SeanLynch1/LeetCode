# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # recursive solution:

        p = root.left
        q = root.right

        def mirror(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True

            if (not p and q) or (p and not q) or (p.val != q.val):
                return False

            output = mirror(p.left, q.right)

            if not output:
                return output

            output = mirror(p.right, q.left)

            return output

        return mirror(p, q)





        # iterative solution:
        ''' stack = []

        p = root.left
        q = root.right

        while stack or p or q:
            while p or q:
                if (not p or not q) or p.val != q.val:
                    return False

                stack.append(p)
                stack.append(q)

                p = p.left
                q = q.right

            q = stack.pop().left
            p = stack.pop().right

        
        return True'''



            

        
