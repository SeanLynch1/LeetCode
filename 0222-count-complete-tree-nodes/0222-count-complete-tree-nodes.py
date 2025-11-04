# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        curr = root
        count = 0

        while curr:

            left, right = curr.left, curr.right
            left_depth = self.count_depth(left)
            right_depth = self.count_depth(right)

            # if right side is possibly imperfect
            if left_depth == right_depth:
                
                count += (2 ** left_depth)
                curr = curr.right
            # if left side is possibly imperfect
            else:
                count += (2 ** right_depth)
                curr = curr.left

        return count

    def count_depth(self, node: TreeNode) -> int:
        num = 0
        while node:
            num += 1
            node = node.left
        
        return num
