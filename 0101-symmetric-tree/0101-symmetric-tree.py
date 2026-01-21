# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([(root.left, root.right)])

        while queue:

            curr_left, curr_right = queue.popleft()

            if not curr_left and not curr_right:
                continue

            if not curr_left or not curr_right:
                return False
            
            if curr_left.val != curr_right.val:
                return False

            queue.append((curr_left.left, curr_right.right))

            queue.append((curr_left.right, curr_right.left))

        return True