class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        i, j = nums_len - 2, nums_len - 1
        while i > -1 and nums[i] >= nums[i + 1]:
            i -= 1
        if i > -1:
            while j > -1 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, nums_len - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
