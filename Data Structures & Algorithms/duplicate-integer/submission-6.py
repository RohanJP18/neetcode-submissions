class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmp = set()
        for i in range(len(nums)):
            if nums[i] in hashmp:
                return True
            hashmp.add(nums[i])
        return False