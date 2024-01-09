class Solution(object):
    def isUnivalTree(self, root):
        def isUnival(root, val):
            if root is None:
                return True
            
            if root.val != val:
                return False
            
            return isUnival(root.left, val) and isUnival(root.right, val)
        
        if root is None:
            return True
        
        return isUnival(root, root.val)