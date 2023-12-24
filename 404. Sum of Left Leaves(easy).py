class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        res = []
        def findLeaf(root, res, where):
            if root == None:
                return
            if root.left == None and root.right == None:
                if where == "left":
                    res.append(root.val)

            findLeaf(root.left, res, 'left')
            findLeaf(root.right, res, 'right')

        findLeaf(root, res, "")
        return sum(res)