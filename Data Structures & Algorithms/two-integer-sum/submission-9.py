class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh_map = {} # number : index

        for index, number in enumerate(nums):
            compliment = target - number
            if compliment in hsh_map:
                return [hsh_map[compliment], index]
            hsh_map[number] = index