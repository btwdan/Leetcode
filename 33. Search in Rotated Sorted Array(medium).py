class Solution(object):
    def search(self, nums, target):
        first = 0
        last = len(nums) - 1
        while True:
            if nums[first] == target:
                return first
            elif nums[last] == target:
                return last
            elif first == last or last == 0 or first == len(nums) - 1:
                break
            else:
                first += 1
                last -= 1

            
        return -1