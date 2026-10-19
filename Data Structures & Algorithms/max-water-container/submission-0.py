class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_total = 0
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            max_total = max(max_total, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_total
            