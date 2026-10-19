class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh_mp = {} # num: index
        
        for index, num in enumerate(nums): # index item
            compliment = target - num
            if compliment in hsh_mp:
                return [hsh_mp[compliment], index]
            hsh_mp[num] = index
