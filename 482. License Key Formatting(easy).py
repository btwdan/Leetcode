class Solution(object):
    def licenseKeyFormatting(self, s, k):
        res = ''
        for i in range(len(s)-1, -1, -1):   
            if s[i] != '-':         
                        
                if len(res) % (k+1) == k:  
                    res += '-'
                res += s[i].upper()   

        return res [::-1]  
        