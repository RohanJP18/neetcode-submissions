class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  
        max_area = 0
        extended_heights = heights + [0]

        for i, h in enumerate(extended_heights):
            while stack and extended_heights[stack[-1]] > h:
                height = extended_heights[stack.pop()]
                
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area