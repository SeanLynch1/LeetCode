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

        stack = []
        curr = root
        h = 0
        nodes = 0

        
        temp = root
        while temp:
            temp = temp.left
            h += 1

        while stack or curr:
            while curr:
                stack.append(curr)
                nodes += 1
                curr = curr.left

            
            if len(stack) == h - 1 and curr is not None:
                print(len(stack))
                print("breaking")
                break

            print("\n")
            # set to 3
            curr = stack.pop()
            curr = curr.right

        return nodes


