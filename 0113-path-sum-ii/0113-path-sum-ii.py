# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        n = targetSum

        def dfs(root: TreeNode, currSum: int) -> List[List[int]]:
            if not root:
                return []

            if not root.left and not root.right:
                if currSum + root.val == n:
                    return [[root.val]]
                if (n < 0 and currSum < n) or (n > 0 and currSum > n):
                    return []
                
            paths = []
            # left  
            left_output = dfs(root.left, currSum + root.val)

            #right
            right_output = dfs(root.right, currSum + root.val)

            for arr in left_output:
                curr = [root.val]
                curr.extend(arr)
                paths.append(curr)

            for arr in right_output:
                curr = [root.val]
                curr.extend(arr)
                paths.append(curr)

            return paths

        return dfs(root, 0)