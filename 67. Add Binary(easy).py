def resultat(x, y):
    res = ""
    t = 0
    for i in range(len(y)):
        if (x[i] == "1" and y[i] == "1"):
            if (t == 1):
                res += "1"
            else:
                res += "0"
                t = 1
        if ((x[i] == "1" and y[i] == "0") or (x[i] == "0" and y[i] == "1")):
            if (t == 1):
                res += "0"
                t = 1
            else:
                res += "1"
        if (x[i] == "0" and y[i] == "0"):
            if(t == 1):
                res += '1'
                t = 0
            else:
                res += '0'

    if (len(x) != len(y)):
        for i in range(len(y), len(x)):
            if (x[i] == '1'):
                if (t == 1):
                    res += '0'
                else:
                    res += '1'
            if (x[i] == '0'):
                if (t == 1):
                    res += '1'
                    t = 0
                else:
                    res += '0'

    if (t == 1):
        res += '1'

    return res[::-1]


class Solution(object):
    def addBinary(self, a, b):
        x = a[::-1]
        y = b[::-1]

        if(len(x) > len(y)):
            return resultat(x, y)
        else:
            return resultat(y, x)

print(Solution().addBinary('1010','1011'))