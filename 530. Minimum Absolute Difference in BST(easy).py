# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        def Spizdyt_derevo(root, num):
            if root == None:
                return
            num.append(root.val)
            Spizdyt_derevo(root.left, num)
            Spizdyt_derevo(root.right, num)

        num = []
        Spizdyt_derevo(root, num)
        print(num)
        minDif = float('inf')
        for i in range (len(num)):
            for j in range (len(num)):
                if num[i] - num[j] < minDif and num[i] - num[j] > 0:
                    minDif = num[i] - num[j]
            j = 0
        return minDif