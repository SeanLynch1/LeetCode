# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        self.found = False

        def helper(node: Optional[TreeNode], curr_sum: int) -> bool:

            if self.found:
                return True

            if not node:
                return False

            curr_sum += node.val


            left = helper(node.left, curr_sum)
            right = helper(node.right,curr_sum)

            print(f"curr_sum = {curr_sum}, left = {left}, right = {right}")

            # found leaf node
            if not left and not right:
                if curr_sum == targetSum:
                    print(f"curr_sum = {curr_sum}")
                    self.found = True

        helper(root, 0)

        return self.found