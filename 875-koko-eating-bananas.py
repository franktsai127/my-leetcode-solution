import math

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            total_time = 0
            mid = (left + right) // 2

            for p in piles:
                total_time += math.ceil(p / mid)

                if total_time > h:
                    break

            if total_time <= h:
                right = mid
            else:
                left = mid + 1
        return left
