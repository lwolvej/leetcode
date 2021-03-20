class Solution:
    def intersection(self, nums1, nums2):
        nums1_set, nums2_set = set(nums1), set(nums2)
        res = []
        for num in nums1_set:
            if num in nums2_set:
                res.append(num)
        return res

    def intersection2(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
