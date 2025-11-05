# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev_val = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev_val)
            self.prev_val = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff
        '''
        # iterative
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
            
        return minimum_distance'''

