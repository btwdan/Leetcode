class Solution(object):
    def isPowerOfTwo(self, n):
        tmp, i = 0, 0
        while tmp < n:
            tmp = 2 ** i
            if tmp == n:
                return True
            i += 1
            

        return False