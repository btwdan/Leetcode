class Solution(object):
    def firstUniqChar(self, s):
        for i in range(len(s)):
            if s[i] not in s[i + 1 : len(s)] and s[i] not in s[0: i]:
                return i

        return -1
        