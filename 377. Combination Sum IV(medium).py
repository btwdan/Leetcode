class Solution(object):
    def combinationSum4(self, nums, target):
        dp = { 0 : 1 }
        for total in range(1, target + 1):
            dp[total] = 0
            for num in nums:
                dp[total] += dp.get(total - num, 0)

        return dp[target]      