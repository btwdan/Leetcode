from collections import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        idx = 0
        for i, j, x in sorted(zip(endTime, startTime, profit)):
            startTime[idx] = j
            endTime[idx] = i
            profit[idx] = x
            idx += 1
        
        for i in range(1, len(profit)):
            index = bisect_right(endTime, startTime[i]) - 1
            profit[i] = max(profit[i - 1], (profit[index] if index >= 0 else 0) + profit[i])

        return profit[-1]