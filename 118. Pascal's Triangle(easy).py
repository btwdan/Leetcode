class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []

        res = [[1]]

        for i in range(1,numRows):
            tmp = [1]
            for j in range(1,i):
                val = res[i-1][j-1] + res[i-1][j]
                tmp.append(val)

            tmp.append(1)
            res.append(tmp) 

        return res