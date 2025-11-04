# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.inorder_mapping = {val: idx for idx, val in enumerate(inorder)}
        self.next_val = 0

        def helper(left, right) -> TreeNode:
           if left >= right:
                return None

           node = TreeNode(preorder[self.next_val])

           mid = self.inorder_mapping[node.val]
           self.next_val += 1

           node.left = helper(left, mid)
           node.right = helper(mid + 1, right)

           return node

        return helper(0, len(preorder))