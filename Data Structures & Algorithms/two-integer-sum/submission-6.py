class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh_mp = {}
        for index in range(len(nums)):
            if (target - nums[index]) in hsh_mp:
                return [hsh_mp[target-nums[index]], index]
            else: 
                hsh_mp[nums[index]] = index