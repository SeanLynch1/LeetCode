# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''if not root:
            return 0

        def getHeight(node):
            height = 0

            while node:
                height += 1
                node = node.left
            return height

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)

        print("left_height = ", left_height)

        if left_height == right_height:
            # when calculating the left we always include the root node
            # left subtree is perfect
            return (2 ** left_height) + self.countNodes(root.right)
        else:
            # right subtree is perfect
            return (2 ** right_height) + self.countNodes(root.left)'''


        # iterative
        stack = []
        curr = root
        nodes = 0
        
        while curr:
            stack.append(curr)
            nodes += 1
            curr = curr.left

        h = nodes

        while stack or curr:
            while curr:
                stack.append(curr)
                nodes += 1
                curr = curr.left
            
            if len(stack) == h - 1 and curr is not None:
                break

            # set to 3
            curr = stack.pop()
            curr = curr.right

        return nodes


