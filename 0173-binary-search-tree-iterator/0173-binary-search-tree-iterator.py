# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        curr = root

        while curr:
            self.stack.append(curr)
            curr = curr.left
        
        curr = self.stack.pop()

        new_node = TreeNode()
        new_node.right = curr
        self.curr = new_node

        return

    def next(self) -> int:
        self.curr = self.curr.right

        while self.stack or self.curr:
            while self.curr:
                self.stack.append(self.curr)
                self.curr = self.curr.left

            self.curr = self.stack.pop()

            return self.curr.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0 or self.curr.right != None
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()