class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            res = res + [[num] + i for i in res]
        return res
