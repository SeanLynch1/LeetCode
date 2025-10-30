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

        self.inorder_map = {}
        self.next_pre = 0

        for idx, val in enumerate(inorder):
            self.inorder_map[val] = idx

        def helper(left,right) -> TreeNode:
            if left >= right:
                return None

            
            val = preorder[self.next_pre]
            node = TreeNode(val)
            mid = self.inorder_map[val]

            # for the next iteration
            self.next_pre += 1

            # next value is to the left of current
            node.left = helper(left, mid)
            # value is the right of current
            node.right = helper(mid + 1, right)

            return node


        self.root = helper(0,len(inorder))

        return self.root