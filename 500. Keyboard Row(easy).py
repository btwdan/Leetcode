class Solution(object):
    def findWords(self, words):
        one = "qwertyuiop"
        two = "asdfghjkl"
        tree = "zxcvbnm"

        res = []

        for i in range(len(words)):
            if len(set(one + words[i].lower())) == len(one):
                res.append(words[i])

            elif len(set(two + words[i].lower())) == len(two):
                res.append(words[i])

            elif len(set(tree + words[i].lower())) == len(tree):
                res.append(words[i])

        return res