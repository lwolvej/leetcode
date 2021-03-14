class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 += nums2
        nums1 = sorted(nums1)
        nums1_len = len(nums1)
        if nums1_len % 2 == 0:
            return (nums1[nums1_len // 2] + nums1[nums1_len // 2 - 1]) / 2
        else:
            return nums1[nums1_len // 2]


