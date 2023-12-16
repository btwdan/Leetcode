class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]

            if d[s[i]] != t[i]:
                return False
        return True