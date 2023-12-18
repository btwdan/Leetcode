class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp, i = 0, 0
        while tmp < n:
            print(tmp)
            tmp = 4 ** i
            if tmp == n:
                return True
            i += 1

        return False
        