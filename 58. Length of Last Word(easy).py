class Solution(object):
    def lengthOfLastWord(self, s):
        LenStr = 0
        count = 0

        for i in range(len(s)):
            if (s[i] == ' '):
                if (count == 0):
                    continue
                else:
                    if (i == len(s) - 1):
                        LenStr = count
                    else:
                        LenStr = count
                        count = 0
            else:
                if(i == len(s) - 1):
                    count += 1
                    LenStr = count
                else:
                    count += 1

        return LenStr