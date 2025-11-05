# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        '''
        # DFS:
        if not root:
            return []
        output = []
        stack = [(root, 1)]

        while stack:
            curr, depth = stack.pop()

            if depth > len(output):
                output.append(curr.val)

            if curr.left:
                stack.append((curr.left, depth + 1))
            if curr.right:
                stack.append((curr.right, depth + 1))
            

        return output
        '''

        # BFS:
        if not root:
            return []
            
        output = []
        queue = deque([root])

        while queue:

            no_nodes_in_level = len(queue)

            for i in range(no_nodes_in_level):
                
                # keep poping the left most node until we reach the final one
                # we need to iterate through each node, to add their children for the next layer
                curr = queue.popleft()
                print(f"curr = {curr}")
                if i == no_nodes_in_level - 1:
                    output.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return output