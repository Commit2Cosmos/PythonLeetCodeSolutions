class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.m = 0

        def recur(node: TreeNode | None):
            if not node:
                return 0
            
            l = recur(node.left)
            r = recur(node.right)

            self.m = max(l + r, self.m)

            return 1 + max(l, r)
        
        recur(root)
        return self.m