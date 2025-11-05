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
        left_to_right = True

        while queue:

            no_nodes_in_level = len(queue)
            slot = []

            for i in range(no_nodes_in_level):
                if left_to_right:
                    curr = queue.popleft()
                else:
                    curr = queue.pop()
                slot.append(curr.val)
            	
                if left_to_right:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                else:
                    if curr.right:
                        queue.appendleft(curr.right)
                    if curr.left:
                        queue.appendleft(curr.left)
                    


            left_to_right = not left_to_right
            output.append(slot)

        return output
