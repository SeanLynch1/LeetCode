# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        nums = []

        stack = [(root, str(root.val))]

        while stack:
            node, string_val = stack.pop()

            if not node.left and not node.right:
                nums.append(int(string_val))

            if node.left:
                stack.append((node.left, string_val + str(node.left.val)))

            if node.right:
                stack.append((node.right, string_val + str(node.right.val)))


        return sum(nums)

        
