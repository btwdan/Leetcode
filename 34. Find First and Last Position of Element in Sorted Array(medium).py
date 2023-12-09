class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        elif len(nums) == 1 and nums[0] != target or nums == []:
            return [-1,-1]

        res = []
        first, last = 0, len(nums) - 1

        while first <= last:
            if nums[first] != target:
                first += 1
            if nums[last] != target:
                last -= 1
            if nums[first] == target and nums[last] == target:
                res.append(first)
                res.append(last)
                break

        if len(res) == 0:
            return [-1, -1]
        return res