# LeetCode Problem 3. Longest Substring Without Repeating Characters (https://leetcode.com/problems/longest-substring-without-repeating-characters/)

def longer_string(s1: str, s2: str) -> str:
    if len(s1) > len(s2):
        return s1
    return s2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_indices = {}
        max_sub = ''
        curr_i = 0
        for i, x in enumerate(s):
            if x not in char_indices:
                char_indices[x] = i
            else:
                if char_indices[x] >= curr_i:
                    max_sub = longer_string(s[curr_i:i], max_sub)
                    curr_i = char_indices[x] + 1
                char_indices[x] = i
        if len(s[curr_i:]) > len(max_sub):
            max_sub = s[curr_i:]

        return len(max_sub)
      
