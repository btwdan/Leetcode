class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) < 1 or len(min(strs)) == 0:
            return ''
        if len(strs) == 1 or len(strs[0]) < 1 or len(set(strs)) == 1:
            return strs[0]  

        if len(min(strs)) == 1:
            for i in range(1, len(strs)):
                if strs[i][0] != strs[0][0]:
                    return ''
            return strs[0][0]

        tmp = strs[0][0]
        res = ''
        j = 0
        count = 0

        while True:
            for i in range(len(strs)):
                if strs[i][j] == tmp:
                    count +=1 

                if i == len(strs) - 1:
                    if count == i + 1:
                        res += strs[i][j]
                        if j == len(min(strs)) - 1:
                            return res
                        j+=1
                        tmp = strs[0][j]
                        count = 0
                    else:
                        return res