class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]

        res = [[1]]

        for i in range(1,rowIndex + 1):
            tmp = [1]
            for j in range(1,i):
                val = res[i-1][j-1] + res[i-1][j]
                tmp.append(val)

            tmp.append(1)
            res.append(tmp) 

        return res[-1]
        