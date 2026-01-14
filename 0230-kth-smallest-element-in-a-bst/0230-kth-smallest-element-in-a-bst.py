# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = [root]
        curr = root
        counter = 0

        while stack or curr:
            while curr.left:
                curr = curr.left
                stack.append(curr)

            curr = stack.pop()
            curr.left = None
            counter += 1

            if counter == k:
                return curr.val

            if curr.right:
                stack.append(curr.right)
                curr = curr.right