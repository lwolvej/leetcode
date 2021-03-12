class Solution:
    def maximumProduct(self, nums):
        nums = sorted(nums)
        nums_len = len(nums)
        if nums[nums_len - 1] < 0:
            return nums[nums_len - 1] * nums[nums_len - 2] * nums[nums_len - 3]
        elif nums[nums_len - 1] == 0:
            if nums_len == 3:
                return 0
            else:
                return nums[nums_len - 4] * nums[nums_len - 2] * nums[nums_len - 3]
        else:
            return max(nums[nums_len - 1] * nums[nums_len - 2]
                       * nums[nums_len - 3], nums[0] * nums[1] * nums[nums_len - 1])
