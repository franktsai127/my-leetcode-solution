from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in pairs]

        fleet = 0
        slowest = 0

        for time in times:
            if time > slowest:
                fleet += 1
                slowest = time

        return fleet
