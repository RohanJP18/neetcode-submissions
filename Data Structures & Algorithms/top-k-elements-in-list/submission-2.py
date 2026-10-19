class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # my solution
        # freq = {} 
        # for i in nums:
        #     if i in freq:
        #         freq[i] += 1
        #     else:
        #         freq[i] = 1
            
        # res = sorted(freq.keys(), key=freq.get, reverse = True)
        # return res[:k]

    # optimal solution

        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
            # [[], [], [], [], [], []]
        
        for num in freq:
            buckets[freq[num]].append(num)

        res = []
        for number in range(len(buckets) - 1, 0, -1):
            for i in buckets[number]:
                res.append(i)
                if len(res) == k:
                    return res
        
                
            
        
