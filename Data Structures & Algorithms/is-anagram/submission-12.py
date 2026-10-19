class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs = [0] * 26
        ct = [0] * 26
        for i in s:
            cs[ord(i) - ord('a')] += 1

        for i in t:
            ct[ord(i) - ord('a')] += 1
            
           
        if cs == ct:
            return True
        return False