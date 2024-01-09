class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        res = 0
        for word in jewels:
            res += stones.count(word)
        
        return res