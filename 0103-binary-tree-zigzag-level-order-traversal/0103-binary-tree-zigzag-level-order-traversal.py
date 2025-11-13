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
            print(f"queue = {queue}")
            for i in range(len(queue)):

                if toggle:
                    curr = queue.pop()
                    print(f"curr = {curr.val}")
                    level_nodes.append(curr.val)

                    if curr.right:
                        queue.appendleft(curr.right)

                    if curr.left:
                        queue.appendleft(curr.left)
                else:
                    curr = queue.popleft()
                    print(f"curr = {curr.val}")
                    level_nodes.append(curr.val)

                    if curr.left:
                        print(f"curr.left = {curr.left.val}")
                        queue.append(curr.left)

                    if curr.right:
                        print(f"curr.right = {curr.right.val}")

                        queue.append(curr.right)

            print("\n")
            output.append(level_nodes)

            toggle = not toggle

        return output