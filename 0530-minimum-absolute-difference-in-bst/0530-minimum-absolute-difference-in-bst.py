# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        minimum_distance = float('inf')

        stack = []

        curr = root

        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if curr.right:
                diff = abs(curr.val - curr.right.val)
            elif stack:
                diff = abs(curr.val - stack[-1].val)

            minimum_distance = min(diff, minimum_distance)
            
            curr = curr.right

        return minimum_distance