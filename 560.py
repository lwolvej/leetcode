# TODO
class Solution:
    def subarraySum(self, nums, k):
        if not nums:
            return 0
        res, mapping, tmp_sum = 0, {}, 0
        mapping[0] = 1
        for i in range(len(nums)):
            tmp_sum += nums[i]
            if (tmp_sum - k) in mapping:
                res += mapping[tmp_sum - k]
            if tmp_sum not in mapping:
                mapping[tmp_sum] = 0
            mapping[tmp_sum] += 1
        return res
