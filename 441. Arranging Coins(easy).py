class Solution(object):
    def arrangeCoins(self, n):
        i = 1
        res = 0
        while n > 0:
            if n - i >= 0:
                res += 1
            n -= i
            i += 1
        return res