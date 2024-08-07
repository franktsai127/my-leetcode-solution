from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, last_idx = stack.pop()
                res[last_idx] = idx - last_idx
            stack.append((temp, idx))

        return res
