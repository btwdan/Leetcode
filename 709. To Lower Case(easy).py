class Solution(object):
    def toLowerCase(self, s):
        res = ''
        for i in range(len(s)):
            if ord(s[i]) >=65 and ord(s[i]) <= 90:
                res += chr(ord(s[i]) + 32)
                continue
            res += s[i]

        return res