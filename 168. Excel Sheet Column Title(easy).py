class Solution(object):
    def convertToTitle(self, columnNumber):
        title = ""
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            title += chr(65 + remainder)
            columnNumber = (columnNumber - 1) // 26
    
        return title[::-1]