class Solution(object):
    def isSubsequence(self, s, t):
        res = 0
        for word in range(len(t)):
            if res < len(s) and s[res] == t[word]:
                res += 1
        return res == len(s)