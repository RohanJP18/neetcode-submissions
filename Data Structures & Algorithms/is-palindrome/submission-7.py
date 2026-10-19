class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        print(s1)
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and s1[l].isalnum() == False:
                l += 1
            while l < r and s1[r].isalnum() == False:
                r -= 1
            if s1[l] != s1[r]:
                print("sl: ", s1[l])
                print("sr: ", s1[r])
                return False
            l += 1
            r -= 1
        
            
        return True