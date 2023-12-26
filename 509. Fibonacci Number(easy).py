class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        elif  n == 1:
            return 1
        curr, next = 0, 1
        res = 0

        for i in range(1, n):
            res = curr + next
            curr, next = next, res
        
        return res