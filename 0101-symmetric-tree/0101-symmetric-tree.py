# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        stack = [(root.left, root.right)]
        
        while stack:
            
            curr_left, curr_right = stack.pop()

            if not curr_left and not curr_right:
                continue

            if (curr_left and not curr_right) or (not curr_left and curr_right):
                return False

            if curr_left.val != curr_right.val:
                return False

            stack.append((curr_left.left, curr_right.right))
            stack.append((curr_left.right, curr_right.left))

        return True
                
