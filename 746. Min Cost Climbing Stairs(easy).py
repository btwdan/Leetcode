class Solution(object):
    def minCostClimbingStairs(self, cost):
        start, prev = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            start, prev = prev, min(start, prev)+cost[i]

        return min(start, prev)