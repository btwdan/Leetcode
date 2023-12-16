class Solution(object):
    def majorityElement(self, nums):
        elementCount = Counter(nums)
        
        res = []
        step = len(nums) // 3
        
        for num, count in elementCount.items():
            if count > step:
                res.append(num)
        
        return res
            