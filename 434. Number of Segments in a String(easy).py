class Solution(object):
    def countSegments(self, s):
        res = 0
        word_count = 0
        for i in range(len(s)):
            if s[i] != " ":
                word_count += 1
            if s[i] == " " and word_count != 0:
                word_count = 0
                res += 1
        if word_count != 0:
            res += 1
        return res