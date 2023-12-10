class Solution:
    def longestPalindrome(self, s):
        def check(i, j):
            l, r = i, j - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                if check(j, j + i):
                    return s[j:j + i]
        return ""