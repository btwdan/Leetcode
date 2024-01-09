class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False

        if len(s) < 2:
            return False

        diff_indices = []
        if len(s) <= 2:
            diff_indices.append(0)
            diff_indices.append(1)

        else:
            if s == goal:
                if len(s) ==len(set(s)):
                    return False
                else:
                    return True

            for i in range(len(s)):
                if s[i] != goal[i]:
                    diff_indices.append(i)
                    
            if len(diff_indices) != 2:
                return False

        swapped_s = list(s)
        swapped_s[diff_indices[0]], swapped_s[diff_indices[1]] = swapped_s[diff_indices[1]], swapped_s[diff_indices[0]]
        swapped_s = ''.join(swapped_s)

        return swapped_s == goal