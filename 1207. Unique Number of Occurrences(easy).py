class Solution(object):
    def uniqueOccurrences(self, arr):
        tmp = set(arr)
        res = []
        for num in tmp:
            res.append(arr.count(num))

        return len(res) == len(set(res))