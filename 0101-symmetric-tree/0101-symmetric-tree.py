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

        stack = []
        
        curr_left = root.left
        curr_right = root.right
        while stack or curr_left or curr_right:
            
            while curr_left and curr_right:
                
                if curr_left.val != curr_right.val:
                    return False

                stack.append(curr_left)
                stack.append(curr_right)

                curr_left = curr_left.left
                curr_right = curr_right.right

            if (curr_left is None and curr_right) or (curr_right is None and curr_left):
                return False

            curr_right = stack.pop()
            curr_left = stack.pop()

            curr_right = curr_right.left
            curr_left = curr_left.right


        return True
                
