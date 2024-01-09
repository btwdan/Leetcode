class Solution:
    def isMonotonic(self, nums):
        isIncreasing = True
        isDecreasing = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                isDecreasing = False
            elif nums[i] < nums[i - 1]:
                isIncreasing = False

        return isIncreasing or isDecreasing