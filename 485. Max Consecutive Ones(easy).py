class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        res = []
        tmp = []
        for num in nums:
            if num == 0:
                if len(tmp) != 0:
                    res.append(tmp)
                    tmp = []
                    continue
                continue
            tmp.append(num)
        if len(tmp) != 0:
            res.append(tmp)
        if len(res) == 0:
            return 0
        max_len = len(res[0])
        for nums in res:
            if len(nums) > max_len:
                max_len = len(nums)
        return max_len
        