class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)


        l =  1
        r = max(piles)
        res = r

        while l <= r:
            k = l + (r - l) // 2
            hours_taken = 0
            for i in range(len(piles)):
                hours_taken += math.ceil(piles[i]/k)
                
            if hours_taken <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res