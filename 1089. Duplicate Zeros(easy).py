class Solution(object):
    def duplicateZeros(self, arr):
        if 0 not in arr:
            return arr

        res = []
        i, j = 0, 0

        while j < len(arr):
            if arr[i] == 0:
                res.append(0)
                res.append(0)
                j += 2
            else:
                res.append(arr[i])
                j += 1

            i += 1

        for i in range(len(arr)):
            arr[i] = res[i]

        return arr