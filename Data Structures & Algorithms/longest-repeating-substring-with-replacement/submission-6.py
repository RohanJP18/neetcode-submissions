class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        seen = {} # char : count
        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]] = 1
            else: 
                seen[s[r]] += 1

            
            if k < r - l + 1 - max(seen.values()): 
                seen[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res

        
