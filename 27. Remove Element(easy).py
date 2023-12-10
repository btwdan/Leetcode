class Solution(object):
    def removeElement(self, nums, val):
        k = nums.count(val)
        for i in range(k):
            nums.remove(val)
        #nums = [el for el in nums if el != val]