class Solution(object):
    def combinationSum(self, candidates, target):
      result = []
    
      def backtrack(start, current_combination, current_sum):
        if current_sum == target:
          result.append(current_combination)
          return
        if current_sum > target:
          return
        for i in range(start, len(candidates)):
          backtrack(i, current_combination + [candidates[i]], current_sum + candidates[i])
            
      backtrack(0, [], 0)
      return result