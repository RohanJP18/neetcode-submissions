class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq : int
        # loop through nums
        # add to freq to arr
        # At the end save each freq and number to dict {number: freq}
        # sort based off key
        # return the kth key! 

        freq = {} 
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        res = sorted(freq.keys(), key=freq.get, reverse = True)
        return res[:k]
        

