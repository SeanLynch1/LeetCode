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
            print(f"root val = {root.val}, currSum = {currSum}")

            if not root.left and not root.right:
                if currSum + root.val == n:
                    return [[root.val]]
                if (n < 0 and currSum < n) or (n > 0 and currSum > n):
                    return []
                

            paths = []
            print(f"currSum + root.val = {currSum + root.val}")
            print("")
            # left  
            left_output = dfs(root.left, currSum + root.val)

            #right
            right_output = dfs(root.right, currSum + root.val)

            for arr in left_output:
                print(f"left arr = {arr}")
                print(f"root val = {root.val}")
                curr = [root.val]
                curr.extend(arr)
                paths.append(curr)
                print("")

            for arr in right_output:
                print(f"right arr = {arr}")
                print(f"root val = {root.val}")
                curr = [root.val]
                curr.extend(arr)
                paths.append(curr)
                print("")

            print(f"paths = {paths}")
            print("")
            return paths

        return dfs(root, 0)