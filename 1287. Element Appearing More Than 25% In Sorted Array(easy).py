class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        lenght = len(arr)
        tf_per = lenght / 4.0

        for num in set(arr):
            if arr.count(num) > tf_per:
                return num
        
        return -1