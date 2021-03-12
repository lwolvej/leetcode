# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        queue = []
        queue.append(root)
        last = root
        res = 0
        while queue:
            cur = queue.pop(0)
            if cur == last:
                res += 1
                if cur.right:
                    last = cur.right
                elif cur.left:
                    last = cur.left
                else:
                    if queue:
                        last = queue[len(queue) - 1]
                    else:
                        return res
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res
                
