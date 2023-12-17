class Solution(object):
    def isPowerOfThree(self, n):
        tmp, i = 0, 0
        while tmp < n:
            print(tmp)
            tmp = 3 ** i
            if tmp == n:
                return True
            i += 1

        return False