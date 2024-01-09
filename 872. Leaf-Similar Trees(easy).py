class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def LST(root, nums):
            if not root:
                return 
            if not root.left and not root.right:
                nums.append(root.val)
            LST(root.left, nums)
            LST(root.right, nums)
        
        nums1 = []
        nums2 = []
        LST(root1, nums1)
        LST(root2, nums2)

        return nums1 == nums2