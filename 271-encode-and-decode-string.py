from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for val in strs:
            res += str(len(val)) + "#" + val
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # use j to find the position of #
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # set i to the beginning of string
            # set j to the end of string
            i = j + 1
            j = i + length
            item = s[i:j]
            res.append(item)
            # move to the next string
            i = j

        return res
