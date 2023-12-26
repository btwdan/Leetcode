class Solution(object):
    def findMaxAverage(self, nums, k):
        s = sum(nums[0 : k])
        max_ = s
        for i in range(0, len(nums) - k):
            s = s + nums[i + k] - nums[i]
            max_ = max(max_, s)
        k *= 1.0
        return max_/ k