class Solution(object):
    def isPerfectSquare(self, num):
        i = 1
        temp = 1
        while i <= num:
            if num == 1:
                return True
            if i == num:
                return True
            temp += 2
            i += temp
        return False