# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder -> node left right
        # inorder -> left node right

        # since preorder records each node straight away, iterate through it, checking left in inorder of the next in preorder gives you what's left of the tree, checking right of the next in preorder gives you what's right of the tree

        # tracks index of preorder list
        self.preorder_idx = 0

        # create inorder dictionary to find what goes left and right of node
        inorder_map = {}

        for idx, val in enumerate(inorder):
            inorder_map[val] = idx


        def tracker(left, right):
            
            if left > right:
                return None

            val = preorder[self.preorder_idx]
            self.preorder_idx += 1
            root = TreeNode(val)

            # to the left of mid is left subtree, to the right of mid is right subtree
            mid = inorder_map[val]
            root.left = tracker(left, mid - 1) # minus 1 as not inclusive
            root.right = tracker(mid + 1, right) # plus 1 as we want to check the next node

            return root

        return tracker(0, len(inorder) - 1)