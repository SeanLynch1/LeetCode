# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    # inorder traversal -> left node right

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        self.pointer = 0
        stack = []
        curr = root

        while stack or curr:
            
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            self.res.append(curr.val)
            curr = curr.right

    def next(self) -> int:
        num = self.res[self.pointer]
        self.pointer += 1
        return num


    def hasNext(self) -> bool:
        return not (self.pointer + 1 > len(self.res))
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()