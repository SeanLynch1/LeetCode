# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue = deque([p, q])

        while queue:
            
            curr_q = queue.popleft()
            curr_p = queue.popleft()

            if not curr_q and not curr_p:
                continue

            if not curr_q or not curr_p:
                return False

            if curr_q.val != curr_p.val:
                return False

            queue.append(curr_p.left)
            queue.append(curr_q.left)

            queue.append(curr_p.right)
            queue.append(curr_q.right)

        return True
