# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        branch = root
        stack = []

        while stack or branch:
            while branch:
                stack.append(branch)

                # swap
                branch.left, branch.right = branch.right, branch.left
                branch = branch.left
            
            branch = stack.pop()
            branch = branch.right

        return root
