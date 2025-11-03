# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        curr = root.left
        max_depth = 1
        val = 1

        while stack or curr:
            
            while curr:
                val += 1
                stack.append((curr, val))
                curr = curr.left

            curr, depth = stack.pop()
            val = depth
            print(f"depth = {depth}")
            curr = curr.right
            max_depth = max(depth, max_depth)
        
        return max_depth

