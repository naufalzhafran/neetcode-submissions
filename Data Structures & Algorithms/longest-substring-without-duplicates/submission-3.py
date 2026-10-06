class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        mem = {}
        
        for right in range(0, len(s)):
            if s[right] in mem:
                left = max(mem[s[right]] + 1, left)
            
            res = max(res, right - left + 1)
            mem[s[right]] = right

            
        return res
