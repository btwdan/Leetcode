class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for num in arr2:
            countEl = arr1.count(num)
            while countEl > 0:
                res.append(num)
                arr1.remove(num)
                countEl -= 1

        if len(arr1) > 0:
            arr1.sort()
            for num in arr1:
                res.append(num)

        return res