class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        res = 0
        hSort = sorted(heights)
        for el1, el2 in zip(heights, hSort):
            if el1 != el2:
                res += 1
        return res