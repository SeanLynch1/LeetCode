# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left_val=None, right_val=None):
#         self.val = val
#         self.left = left_val
#         self.right = right_val
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.min_abs = float('inf')

        def helper(node: TreeNode, last_val: int) -> int:
            
            curr_val = node.val
            self.min_abs = min(self.min_abs, abs(curr_val - last_val))

            if node.left:
                left_val = helper(node.left, last_val)
                self.min_abs = min(self.min_abs, abs(curr_val - left_val))

            if node.right:
                right_val = helper(node.right, curr_val)
                self.min_abs = min(self.min_abs, abs(curr_val - right_val))
                return right_val

            return curr_val

        helper(root, float('inf'))
        return self.min_abs