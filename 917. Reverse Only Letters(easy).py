class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        onlyCh = ''
        isFrom = []
        inWhere = []
        for i, ch in enumerate(s):
            if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
                onlyCh += ch
            else:
                isFrom.append(ch)
                inWhere.append(i)
        res = ''
        onlyCh = onlyCh[::-1]
        i, j, n = 0, 0, 0
        while n < len(s):
            if j < len(inWhere) and n == inWhere[j]:
                res += str(isFrom[j])
                j += 1
                n += 1
                continue
            res += onlyCh[i]
            i += 1
            n += 1
        return res