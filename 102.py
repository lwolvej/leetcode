import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode):
        d = {}

        def f(r, i):
            if r:
                if i in d:
                    d[i].append(r.val)
                else:
                    d[i] = [r.val]
                f(r.left, i + 1)
                f(r.right, i + 1)
        f(root, 0)
        return [*d.values()]
