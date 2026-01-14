# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # inorder traversal

        def inorder(node: TreeNode, low: int, high:int) -> bool:
            
            if low >= node.val or high <= node.val:
                return False

            # left
            if node.left:
                if node.left.val >= node.val:
                    return False

                left = inorder(node.left, low, node.val)

                if not left:
                    return False

            # right
            if node.right:
                    
                right = inorder(node.right, node.val, high)

                if not right:
                    return False

            return True
        
        return inorder(root, float('-inf'), float('inf'))