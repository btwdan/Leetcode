class Solution(object):
    def pivotIndex(self, nums):
        i, j = 0, sum(nums)
        for index, elem in enumerate(nums):
            j -= elem
            if i == j:
                return index
            i += elem
        return -1  