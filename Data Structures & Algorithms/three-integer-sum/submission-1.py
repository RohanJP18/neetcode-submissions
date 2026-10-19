class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                sum_3 = sorted_nums[l] + sorted_nums[i] + sorted_nums[r]
                if sum_3 == 0:
                    if [sorted_nums[i], sorted_nums[l], sorted_nums[r]] not in res:
                        res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                elif sum_3 < 0:
                    l += 1
                elif sum_3 > 0:
                    r -= 1
                
        return res