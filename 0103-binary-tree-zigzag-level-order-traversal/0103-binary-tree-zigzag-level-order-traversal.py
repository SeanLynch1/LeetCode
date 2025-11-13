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
        toggle = False

        while queue:
            level_nodes = []

            for i in range(len(queue)):
                curr = queue.popleft()
                level_nodes.append(curr.val)

                if toggle:
                    if curr.left:
                        queue.append(curr.left)

                    if curr.right:
                        queue.append(curr.right)
                else:
                    if curr.right:
                        queue.append(curr.right)

                    if curr.left:
                        queue.append(curr.left)

            output.append(level_nodes)

            toggle = not toggle

        return output