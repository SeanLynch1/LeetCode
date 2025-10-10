# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # inorder -> left node right
        # postorder -> left right node

        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def helper(left, right):
            
            if left > right:
                return None

            val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(val)

            mid = inorder_map[val]

            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(postorder) - 1) # 4