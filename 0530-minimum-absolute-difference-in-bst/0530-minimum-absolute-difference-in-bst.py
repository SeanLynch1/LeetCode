# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        min_diff = float('inf')
        stack = []
        curr = root
        prev = float('inf')

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            min_diff = min(min_diff, abs(curr.val - prev))
            print(f"min_diff = {min_diff}")
            prev = curr.val
            curr = curr.right

        return min_diff