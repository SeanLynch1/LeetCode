# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        output = []
        toggle = True

        while queue:
            
            temp = []
            for i in range(len(queue)):
                if toggle:
                    curr = queue.popleft()
                    temp.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    
                    if curr.right:
                        queue.append(curr.right)
                else:
                    curr = queue.pop()
                    temp.append(curr.val)

                    if curr.right:
                        queue.appendleft(curr.right)

                    if curr.left:
                        queue.appendleft(curr.left)

            toggle = not toggle
            output.append(temp)

        return output