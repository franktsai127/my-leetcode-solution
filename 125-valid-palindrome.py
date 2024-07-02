class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # check left is alnum
            while left < right and not self.is_al_num(s[left]):
                left += 1
            # check right is alnum
            while left < right and not self.is_al_num(s[right]):
                right -= 1

            if left < right and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def is_al_num(self, val: str):
        return (
            ord("a") <= ord(val) <= ord("z")
            or ord("A") <= ord(val) <= ord("Z")
            or ord("0") <= ord(val) <= ord("9")
        )
