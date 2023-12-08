class Solution(object):
    def romanToInt(self, s):
        sum = 0
        a = list(s)
        for i in range(len(s)):
            if(s[i] == "I"):
                sum += 1
            if(s[i] == "V"):
                if(s[i-1] == "I" and i != 0):
                    sum -= 1
                    sum += 4
                else:
                    sum += 5
            if(s[i] == "X"):
                if(s[i-1] == "I" and i != 0):
                    sum -= 1
                    sum += 9
                else:
                    sum += 10
            if(s[i] == "L"):
                if(s[i-1] == "X" and i != 0):
                    sum -= 10
                    sum += 40
                else: 
                    sum += 50
            if(s[i] == "C"):
                if(s[i-1] == "X" and i != 0):
                    sum -= 10
                    sum += 90
                else:
                    sum += 100
            if(s[i] == "D"):
                if(s[i-1] == "C" and i != 0):
                    sum -= 100
                    sum += 400
                else: 
                    sum += 500
            if(s[i] == "M"):
                if(s[i-1] == "C" and i != 0):
                    sum -= 100
                    sum += 900
                else:
                    sum += 1000
        return sum