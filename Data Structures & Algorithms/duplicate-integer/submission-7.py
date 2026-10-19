class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash_mp -> number: index
        # iterate through nums
        # if seen in hsh_mp return true
        # if not seen add to hsh_mp


        hsh_mp = {}

        for index, number in enumerate(nums):
            if number in hsh_mp:
                return True
            hsh_mp[number] = index
        return False