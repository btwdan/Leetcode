class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        temp_str = ""

        for i in range(len(s)):
            if (ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >= 48 and ord(s[i]) <= 57):
                temp_str += s[i]

        return temp_str == temp_str[::-1]