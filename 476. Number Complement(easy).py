class Solution(object):
    def findComplement(self, num):
        def binary(num):
            res = ''

            while num > 0:
                res += str(num % 2)
                num //= 2

            return res
            
        tmp = binary(num)
        sec_num = tmp[::-1]
        res = ''
        isTrue = True

        for i in range(len(sec_num)):
            if isTrue:
                if sec_num[i] == '1':
                    isTrue = False
                else:
                    continue

            if sec_num[i] == '1':
                res += '0'
            if sec_num[i] == '0':
                res += '1'

        return int(res, 2)