class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            temp = 0
            for i in range(len(str(num))):
                temp += int(str(num)[i])
            num = temp
        return num