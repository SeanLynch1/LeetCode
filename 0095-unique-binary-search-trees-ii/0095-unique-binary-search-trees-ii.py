# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def dfs(start: int, end: int) -> List[Optional[TreeNode]]:

            if start > end:
                return [None]

            trees = []
            for i in range(start, end + 1):

                left_trees = dfs(start, i - 1)
                right_trees = dfs(i + 1, end)

                for l in left_trees:
                    for r in right_trees:

                        root = TreeNode(i)
                        root.left = l
                        root.right = r

                        trees.append(root)

            return trees

        return dfs(1, n)