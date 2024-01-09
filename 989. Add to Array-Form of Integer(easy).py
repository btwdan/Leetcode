class Solution(object):
    def addToArrayForm(self, num, k):
        newNum = num
        splitNum = 0

        for i in range(len(newNum)):
            splitNum *= 10
            splitNum += newNum[i]

        res = []
        splitNum += k
        i = 0

        while(splitNum != 0):
            res.append(splitNum % 10)
            splitNum //= 10
            i += 1

        return res[::-1]