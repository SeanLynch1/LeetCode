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

        def mirror(p_root: Optional[TreeNode], q_root: Optional[TreeNode]) -> bool:
            if not p_root and not q_root:
                return True

            if (not p_root and q_root) or (p_root and not q_root) or (p_root.val != q_root.val):
                return False

            p = p_root.left
            q = q_root.right

            output = mirror(p, q)

            if not output:
                return output

            p = p_root.right
            q = q_root.left

            output = mirror(p, q)

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



            

        
