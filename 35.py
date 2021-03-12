class Solution:
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        if nums[0] > target:
            return 0
        i = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if i + 1 < len(nums) and nums[i] < target < nums[i + 1]:
                return i + 1
        return 0