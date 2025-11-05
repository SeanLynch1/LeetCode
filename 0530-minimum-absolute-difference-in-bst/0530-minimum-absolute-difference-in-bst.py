# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        minimum_distance = float('inf')

        inorder_vals = []
        stack = []

        curr = root

        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            inorder_vals.append(curr.val)

            if len(inorder_vals) > 1:
                diff = abs(inorder_vals[-1] - inorder_vals[-2])
                minimum_distance = min(diff, minimum_distance)

            curr = curr.right
            
        return minimum_distance