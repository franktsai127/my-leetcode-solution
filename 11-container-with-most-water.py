from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        max_product = 0

        while left < right:
            left_val = heights[left]
            right_val = heights[right]
            x_axis = right - left

            if left_val < right_val:
                y_axis = left_val
                left += 1
            else:
                y_axis = right_val
                right -= 1

            result = x_axis * y_axis

            if result > max_product:
                max_product = result

        return max_product
