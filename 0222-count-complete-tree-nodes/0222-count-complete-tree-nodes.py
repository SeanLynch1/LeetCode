# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        curr = root
        
        while curr:
            left, right = curr.left, curr.right
            left_depth = self._depth(left)
            right_depth = self._depth(right)
            
            if left_depth == right_depth:
                # Left subtree is perfect
                count += 1 << left_depth  # 2^left_depth
                curr = curr.right
            else:
                # Right subtree is perfect
                count += 1 << right_depth  # 2^right_depth
                curr = curr.left
                
        return count

    def _depth(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth

