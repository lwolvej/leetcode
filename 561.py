class Solution:
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        i, res = 0, 0
        while i < len(nums):
            res += min(nums[i], nums[i + 1])
            i += 2
        return res

    def arrayPairSum2(self, nums):
        return sum(sorted(nums)[::2])
