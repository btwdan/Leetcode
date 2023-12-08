class Solution(object):
    def reverse(self, x):
        if '-' in str(x):
            str_int = ""
            for i in range(1, len(str(x))):
                str_int += str(x)[i]
            res = int(str_int[::-1]) - (int(str_int[::-1]) * 2)
            if res > 2**31 - 1 or res < -2**31:
                return 0
            return res
        else:
            if int(str(x)[::-1]) > 2**31 - 1 or int(str(x)[::-1]) < -2**31:
                return 0
            return int(str(x)[::-1])