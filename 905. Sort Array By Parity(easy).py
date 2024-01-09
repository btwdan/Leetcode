class Solution(object):
    def sortArrayByParity(self, nums):
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                for j in range(i, len(nums)):
                    if nums[j] % 2 == 0:
                        nums[i], nums[j] = nums[j], nums[i]

        return nums