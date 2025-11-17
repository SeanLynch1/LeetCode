# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        queue = deque([root])
        curr_node = None
        output = []

        while queue:
            for i in range(len(queue)):
                curr_node = queue.popleft()
                
                # add left
                if curr_node.left:
                    queue.append(curr_node.left)

                # add right
                if curr_node.right:
                    queue.append(curr_node.right)
                
            output.append(curr_node.val)
            
        return output