# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        output = []
        queue = deque([root])

        while queue:
            
            no_nodes_in_level = len(queue)
            slot = []
            for i in range(len(queue)):
                curr = queue.popleft()
                slot.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            
            output.append(slot)

        return output
        