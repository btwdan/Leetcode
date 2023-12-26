class Solution(object):
    def hammingDistance(self, x, y):
        res = 0
        bin_x = format(x, 'b')
        bin_y = format(y, 'b')
        max_bin = max(len(bin_x), len(bin_y))
        if len(bin_x) < max_bin:
            bin_x = '0'*(max_bin - len(bin_x)) + bin_x
        if len(bin_y) < max_bin:
            bin_y = '0'*(max_bin - len(bin_y)) + bin_y
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                res += 1

        return res