# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and root.right or root.left and not root.right:
            return False

        if not root.left and not root.right:
            return True

        queue = deque([(root.left, root.right)])

        while queue:

            curr_left, curr_right = queue.popleft()

            if (not curr_left.left and curr_right.right) or (not curr_right.right and curr_left.left):
                return False
            
            if (not curr_left.right and curr_right.left) or (curr_left.right and not curr_right.left):
                return False

            if curr_left.val != curr_right.val:
                return False

            if curr_left.left and curr_right.right:
                queue.append((curr_left.left, curr_right.right))

            if curr_right.left and curr_left.right:
                queue.append((curr_left.right, curr_right.left))

        return True