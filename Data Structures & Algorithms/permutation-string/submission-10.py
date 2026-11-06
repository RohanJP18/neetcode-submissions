class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fill freq map for s1
        s1_f = [0] * 26
        for i in s1:
            s1_f[ord(i) - ord('a')] += 1

        window = len(s1)
        # loop through s2
        
        l = 0
        for r in range(window, len(s2)+1):
            s2_f = [0] * 26
            for i in s2[l:r]:
                s2_f[ord(i) - ord('a')] += 1
            if s1_f == s2_f:
                return True
            l += 1
        return False
