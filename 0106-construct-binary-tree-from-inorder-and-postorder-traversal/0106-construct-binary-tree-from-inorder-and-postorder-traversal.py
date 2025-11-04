# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # postorder is preorder but backwards

        self.inorder_mapping = {val: idx for idx, val in enumerate(inorder)}

        self.next_val = len(postorder) - 1

        def helper(left, right) -> TreeNode:
            
            if left >= right:
                return None

            node = TreeNode(postorder[self.next_val])

            mid = self.inorder_mapping[node.val]
            self.next_val -= 1

            node.right = helper(mid + 1, right)
            node.left = helper(left, mid)

            return node

        return helper(0, len(postorder))

        