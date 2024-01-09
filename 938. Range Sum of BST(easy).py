class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(root, nums):
            if not root:
                return 
            
            if root.val > nums[0] and root.val < nums[1]:
                nums.append(root.val)

            dfs(root.left, nums)
            dfs(root.right, nums)
        
        nums = [low, high]
        dfs(root, nums)

        return sum(nums)