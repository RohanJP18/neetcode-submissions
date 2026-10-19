class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # prefix
         
        prefix = 1
        pre_arr = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                pre_arr[i] = nums[i]
            pre_arr[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        post_arr = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post_arr[i] = nums[i]
            post_arr[i] = postfix
            postfix *= nums[i]

        for i in range(len(nums)):
            res[i] = post_arr[i] * pre_arr[i]
            
        return res
