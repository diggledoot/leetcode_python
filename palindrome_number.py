class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_str = str(x)

        if len(int_str) == 1:
            return True

        if ["-", "+"] in list(int_str):
            return False

        if int_str[::-1][0] == "0":
            return False

        if int_str == int_str[::-1]:
            return True
