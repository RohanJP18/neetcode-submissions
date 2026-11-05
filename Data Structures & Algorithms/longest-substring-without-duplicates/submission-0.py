class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 0
        max_str = 0
        curr_window = 0
        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                r += 1
                curr_window = r - l
                max_str = max(curr_window, max_str)
        
        return max_str