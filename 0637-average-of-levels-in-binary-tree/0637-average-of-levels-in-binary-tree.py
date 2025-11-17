# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        

        queue = deque([root])
        output = []


        while queue:
            
            nodes = len(queue)
            summation = 0
            for i in range(nodes):
                curr = queue.popleft()

                summation += curr.val

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)
            
            output.append(summation/ nodes)

        return output
            


