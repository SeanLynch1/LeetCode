# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        print("hey")
        if root.left:
            right_most = root.left

            print("hi")
            while right_most.right:
                right_most = right_most.right

            right_most.right = root.right

            root.left, root.right = None, root.left

        print(f"root.val = {root.val}")
        self.flatten(root.right)