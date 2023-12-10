class Solution(object):
    def plusOne(self, digits):
        count = 1
        newDig = digits[::-1]
        res = []

        for i in range(len(newDig)):
            if(count != 0):
                sum = newDig[i] + count
                if(sum <= 9):
                    res.append(sum)
                    count = 0
                else:
                    res.append(sum - 10)
            else:
                res.append(newDig[i])

        if(count == 1):
            res.append(1)


        return res[::-1]