# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        return self.validate(root, -sys.maxsize - 1, sys.maxsize)

    def validate(self, node, min_num, max_num):
        if not node:
            return True
        if node.val <= min_num or node.val >= max_num:
            return False
        return self.validate(node.left, min_num, node.val) and self.validate(node.right, node.val, max_num)
