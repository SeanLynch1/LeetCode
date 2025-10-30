# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        stack = []
        curr = root
        val = 0

        while stack or curr:

            while curr:
                val += curr.val
                stack.append(curr)
                curr = curr.left
            
            
                
            curr = stack.pop()

            print(f"val = {val}")
            print("\n")

            if not curr.left and not curr.right:
                if val == targetSum:
                    return True
            
            if not curr.right:
                val -= curr.val

            curr = curr.right
            
            

        return False