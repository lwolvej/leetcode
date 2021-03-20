import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        d = collections.defaultdict(list)

        def f(r, i):
            if r:
                d[i].append(r.val)
                f(r.left, i + 1)
                f(r.right, i + 1)
        f(root, 1)
        res = [*d.values()]
        for i in range(len(res)):
            if i % 2 != 0:
                res[i].reverse()
        return res
