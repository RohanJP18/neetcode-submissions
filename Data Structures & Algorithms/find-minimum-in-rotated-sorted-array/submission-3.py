class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            
            m = l + (r - l) // 2
            
            print(nums[l],nums[m], nums[r])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            print("adjusted: ", nums[l], nums[m], nums[r])

        return nums[r]