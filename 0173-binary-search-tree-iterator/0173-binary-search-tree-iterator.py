# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.curr = root
        self.stack = []

        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left
        
        
    def next(self) -> int:
        if self.curr:
            self.curr = self.curr.right
        
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        self.curr = self.stack.pop()
        val = self.curr.val

        return val

    def hasNext(self) -> bool:
        return not( not self.stack and (not self.curr or not self.curr.right))

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()