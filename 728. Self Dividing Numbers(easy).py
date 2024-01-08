class Solution(object):
    def selfDividingNumbers(self, left, right):
        def isDividing(num):
            num_str = str(num)
            for i in range(len(num_str)):
                if '0' in num_str:
                    return False
                if num % int(num_str[i]) != 0:
                    return False
            return True
        res = []
        for i in range(left, right + 1):
            if isDividing(i):
                res.append(i)
        return res

        