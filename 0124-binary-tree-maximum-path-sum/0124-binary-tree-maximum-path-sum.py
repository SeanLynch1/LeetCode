# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = root.val

        def helper(node: TreeNode) -> int:

            if not node:
                return 0
            
            val = node.val

            left = helper(node.left) # 30
            right = helper(node.right) # 4
            
            left_sum = left + val # 39
            right_sum = right + val # 4

            outcome = max(val,max(left_sum, right_sum)) # 39

            left_right_sum = left + right + val # 43

            if left_right_sum > outcome:
                self.max_sum = max(left_right_sum, self.max_sum)
            else:
                self.max_sum = max(outcome, self.max_sum)
                
            return outcome


        helper(root)

        return self.max_sum
