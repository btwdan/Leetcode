class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        resArr = []
        
        for i in range(len(nums)):
            resArr.append(True) if int(str(nums[0:i]), 2) % 5 == 0 else resArr.append(False)

        return resArr