class Solution(object):
    def findTheDifference(self, s, t):
        if len(s) < len(t):
            for word in s:
                if word in t:
                    t = t.replace(word, "", 1)
            return t

        else:
            for word in t:
                if word in s:
                    s = s.replace(word, "", 1)
            return s