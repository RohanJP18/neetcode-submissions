class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh_mp = {}
        
        for index, number in enumerate(nums):
            compliment = target - number
            if compliment in hsh_mp:
                return [hsh_mp[compliment], index]
            hsh_mp[number] = index
