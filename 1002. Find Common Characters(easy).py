class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words[0])):
            ch = words[0][i]
            isInAll = True
            for j in range(1, len(words)):
                if ch not in words[j]:
                    isInAll = False
                words[j] = words[j].replace(ch, '', 1)
            if isInAll:
                res.append(ch)
        
        return res