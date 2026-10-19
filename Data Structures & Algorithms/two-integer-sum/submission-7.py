class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # number,index  
        hsh_mp = {}

        # loop through
        for index, number in enumerate(nums): # index, number
            # save compliment
            compliment = target - number
            # check if compliment in map if so return 
            if compliment in hsh_mp:
                return [hsh_mp[compliment], index]
            # if not save compliment in hash_map
            hsh_mp[number] = index
        


