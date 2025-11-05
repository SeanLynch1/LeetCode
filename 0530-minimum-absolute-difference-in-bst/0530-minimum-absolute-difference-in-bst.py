# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        minimum_distance = float('inf')

        prev_val = None
        stack = []

        curr = root

        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if prev_val is not None:
                minimum_distance = min(abs(curr.val - prev_val), minimum_distance)

            prev_val = curr.val
            curr = curr.right
            
        return minimum_distance