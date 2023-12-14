class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for word in columnTitle:
            res = res * 26 + (ord(word) - 64)

        return res
        