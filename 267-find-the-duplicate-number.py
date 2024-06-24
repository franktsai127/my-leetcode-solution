from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        existed_dict = dict()
        for n in nums:
            if n not in existed_dict:
                existed_dict[n] = True
            else:
                return n
