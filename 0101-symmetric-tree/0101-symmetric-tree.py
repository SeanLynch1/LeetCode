# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # iterative
        stack = [(root.left, root.right)]

        while stack:
            curr_left, curr_right = stack.pop()

            if not curr_left and not curr_right:
                continue
            elif not curr_left or not curr_right:
                return False
            elif curr_left.val != curr_right.val:
                return False

            stack.append((curr_left.right, curr_right.left))
            stack.append((curr_left.left, curr_right.right))

        
        return True




        # recursive
        '''def helper(left_node, right_node):
            if not left_node and not right_node:
                return True
            elif not left_node or not right_node:
                return False
            elif left_node.val != right_node.val:
                return False

            if not helper(left_node.left, right_node.right):
                return False

            if not helper(left_node.right, right_node.left):
                return False

            return True
        
        return helper(root.left, root.right)'''



        