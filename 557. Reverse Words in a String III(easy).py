class Solution(object):
    def reverseWords(self, s):
        words = []
        word = ''
        for i in range(len(s)):
            if i == len(s) - 1:
                word += s[i]
                words.append(word)
            if s[i] == ' ':
                words.append(word)
                word = ''
                continue
            word += s[i]
        res = ''
        for i in range(len(words)):
            res += words[i][::-1]
            if i == len(words) - 1:
                break
            res += " "
        return res