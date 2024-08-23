from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s_matrix = sum(matrix, [])

        left = 0
        right = len(s_matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if s_matrix[mid] < target:
                left = mid + 1
            elif s_matrix[mid] > target:
                right = mid - 1
            else:
                return True

        return False
