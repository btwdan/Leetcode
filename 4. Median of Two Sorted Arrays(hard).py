class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 += nums2
        nums1.sort()
        lenth = len(nums1)

        if lenth % 2 == 0:
            first = lenth / 2
            res = (nums1[first] + nums1[first - 1]) / 2.0
            return res
        else:
            b = lenth // 2
            return nums1[b]