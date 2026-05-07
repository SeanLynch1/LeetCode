# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []

        def dfs(node: TreeNode, path: List[str]) -> None:
            path.append(str(node.val))

            if not node.left and not node.right:
                res.append("->".join(path))
                path.pop()
                return
            
            # left 
            if node.left:
                dfs(node.left, path)

            # right
            if node.right:
                dfs(node.right, path)

            path.pop()


        dfs(root, [])
        return res