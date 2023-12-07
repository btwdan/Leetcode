class Solution(object):
    def lengthOfLongestSubstring(self,s):
      char_dict = {}
      left = 0
      max_len = 0
    
      for right in range(len(s)):
        if s[right] in char_dict and char_dict[s[right]] >= left:
          left = char_dict[s[right]] + 1
        char_dict[s[right]] = right
        max_len = max(max_len, right - left + 1)
        
      return max_len