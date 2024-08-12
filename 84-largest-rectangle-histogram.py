from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                prev_idx, prev_height = stack.pop()
                max_area = max(max_area, (idx - prev_idx) * prev_height)
                start = prev_idx
            stack.append((start, height))

        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)

        return max_area
