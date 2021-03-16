class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -10000000

        def get_max(self, root: TreeNode) -> int:
            if root:
                left = max(0, self.get_max(root.left))
                right = max(0, self.get_max(root.right))
                self.res = max(self.res, root.val + left + right)
                return max(left, right) + root.val
            else:
                return 0
        get_max(root)
        return self.res
