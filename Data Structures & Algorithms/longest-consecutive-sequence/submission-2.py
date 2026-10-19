class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for number in num_set:
            length = 0
            if number - 1 not in num_set:
                curr = number
                length += 1

                while curr + 1 in num_set:
                    curr += 1
                    length += 1
            max_length = max(length, max_length)

        return max_length

       
            
            
