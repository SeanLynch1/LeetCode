# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_curr = root.left
        left_depth = 0
        # find left_curr of far left of left side
        while left_curr:
            left_curr = left_curr.left
            left_depth += 1
        
        # find depth of far left on right side
        right_curr = root.right
        right_depth = 0

        while right_curr:
            right_curr = right_curr.left
            right_depth += 1

        stack = []
        # right side is possibly imperfect
        if right_depth == left_depth:
            depth = (2 ** left_depth)
            curr = root.right

            while stack or curr:
                while curr:
                    depth += 1
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop().right

            print("HI")

        # left side is possibly imperfect
        else:
            print(f"right_depth = {right_depth}")
            depth = (2 ** right_depth)
            print(f"depth = {depth}")
            curr = root.left

            while stack or curr:
                while curr:
                    depth += 1
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop().right

        return depth

