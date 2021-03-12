class Solution:
    def findMaxConsecutiveOnes(self, nums):
        tmp_res, res = 0, 0
        for num in nums:
            if num == 1:
                tmp_res += 1
            else:
                tmp_res = 0
            res = max(tmp_res, res)
        return res