# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative
        if not root:
            return 0

        depth = 1
        max_depth = 1
        stack = [(root, depth)]
        curr = root.left
        while stack or curr:
            while curr:
                depth += 1
                stack.append((curr, depth))
                curr = curr.left
            curr, depth = stack.pop()
            curr = curr.right

        return max_depth
        # recursive
        '''if not root:
            return 0
        
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left,right)'''
        
        