# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {}

        for i in range(len(inorder)):
            mapping[inorder[i]] = i

        self.pos = 0

        def check_sides(left: int, right: int) -> TreeNode:

            if left > right:
                return None
          
            val = preorder[self.pos]
            idx = mapping[val]

            new_node = TreeNode(val)

            self.pos += 1
            
            new_node.left = check_sides(left, idx - 1)
            new_node.right = check_sides(idx + 1, right)

            return new_node

        return check_sides(0, len(inorder)-1)
