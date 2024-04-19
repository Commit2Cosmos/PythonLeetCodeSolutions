class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution:
    def maxDepthDFS(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepthDFS(root.left), self.maxDepthDFS(root.right))
    

    def maxDepthBFS(self, root: TreeNode)-> int:

        if not root:
            return 0

        lvl = 0
        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            lvl += 1

        return lvl
    

    def maxDepthIterDFS(self, root: TreeNode)-> int:

        if not root:
            return 0

        stack = [[root, 1]]
        res = 0

        while stack:
            node, lvl = stack.pop()
            res = max(res, lvl)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res