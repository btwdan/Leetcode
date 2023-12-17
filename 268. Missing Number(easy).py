class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(1, n):
            print('enter', nums[i])
            if nums[i] - 1 != nums[i - 1]:
                return nums[i] - 1
            if i == n - 1:
                return n
        return 1 if 0 in nums else 0