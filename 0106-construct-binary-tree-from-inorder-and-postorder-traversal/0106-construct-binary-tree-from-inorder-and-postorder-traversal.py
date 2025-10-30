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

        inorder_map = {}

        for idx, val in enumerate(inorder):
            inorder_map[val] = idx

        self.next_idx = len(inorder) - 1

        def helper(left, right) -> TreeNode:
            if left >= right:
                return None

            val = postorder[self.next_idx]
            self.next_idx -= 1

            node = TreeNode(val)
            mid = inorder_map[val]
            
            node.right = helper(mid + 1, right)
            node.left = helper(left, mid)

            return node

        
        return helper(0, len(inorder))


                