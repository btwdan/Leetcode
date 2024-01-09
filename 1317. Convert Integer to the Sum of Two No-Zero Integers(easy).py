class Solution(object):
    def getNoZeroIntegers(self, n):
        num_1, num_2 = 0, n
        i = 1
        
        while True:
            if '0' not in str(num_1) and '0' not in str(num_2):
                return [num_1, num_2]
            
            num_1 = n - i
            num_2 = n - num_1
            i+=1
        
        return -1