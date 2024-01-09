class Solution(object):
    def uniqueMorseRepresentations(self, words):
        new_alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                    ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                    "...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        d = {}
        for i in range(len(new_alpha)):
            d[alphabet[i]] = new_alpha[i]

        print(d)
        res = set()
        for word1 in words:
            tmp = ''
            for word2 in word1:
                tmp += d[word2]
            res.add(tmp)
        
        return len(res)