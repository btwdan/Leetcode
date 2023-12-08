class Solution(object):
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            square = (j - i) * min(height[i], height[j])
            print(i, j)
            if square > res:
                res = square

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res