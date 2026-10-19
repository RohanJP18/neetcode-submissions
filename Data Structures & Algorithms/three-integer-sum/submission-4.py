class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
                
            l = i + 1
            r = len(sorted_nums) - 1

            while l < r:
                sum_3 = sorted_nums[l] + sorted_nums[i] + sorted_nums[r]
                if sum_3 == 0:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                elif sum_3 < 0:
                    l += 1
                elif sum_3 > 0:
                    r -= 1
                

                
        return res