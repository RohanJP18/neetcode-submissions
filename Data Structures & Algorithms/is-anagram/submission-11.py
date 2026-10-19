class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)
        count2 = Counter(t)
        if len(s) == len(t):
            if count2 == count:
                return True
            else:
                return False
        return False