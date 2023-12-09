class Solution(object):
    def searchInsert(self, nums, target):
        first, last = 0,len(nums)-1
        while True:
            if nums[first] >= target:
                return first
            if nums[last] < target:
                return last + 1
            if nums[last] == target:
                return last

            if nums[first] > target and target < nums[last]:
                return first

            if nums[first] < target:
                first += 1
            if nums[last] > target:
                last -= 1