# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Recursive


        def dfs(node, curr_sum):

            if not node:
                return 0
            
            curr_sum = (curr_sum * 10) + node.val
            print(f"curr_sum = {curr_sum}")

            if not node.left and not node.right:
                return curr_sum

            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)


        return dfs(root, 0)



        # Iterative
        '''total = 0
        stack = [(root, str(root.val))]

        while stack:
            node, string_val = stack.pop()

            if not node.left and not node.right:
                total += int(string_val)

            if node.left:
                stack.append((node.left, string_val + str(node.left.val)))

            if node.right:
                stack.append((node.right, string_val + str(node.right.val)))


        return total'''

        
