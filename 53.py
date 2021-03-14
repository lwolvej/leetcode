class Solution:
    def maxSubArray(self, nums):
        res, tmp_res = nums[0], 0
        for num in nums:
            if tmp_res > 0:
                tmp_res += num
            else:
                tmp_res = num
            res = max(res, tmp_res)
        return res

    def maxSubArray2(self, nums):
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]
        dd = [0] * nums_len
        dd[0] = nums[0]
        for i in range(1, nums_len):
            dd[i] = max(dd[i - 1] + nums[i], nums[i])
        return max(dd)
