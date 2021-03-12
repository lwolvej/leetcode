class Solution:
    def findDuplicate(self, nums):
        if not nums:
            return 0
        mapping = {}
        for num in nums:
            if num in mapping:
                return num
            else:
                mapping[num] = 1
        return 0