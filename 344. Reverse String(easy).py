class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while True:
            if left == right or left > right:
                break

            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp

            left += 1
            right -= 1
            
        return s