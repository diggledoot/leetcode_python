class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False

        if x < 0:
            is_negative = True
            x = abs(x)

        reversed_n = int(str(x)[::-1]) #convert to string reverse it and convert back to integer

        #Compensate for integer overflow
        if reversed_n >= 2 ** 31 - 1 or reversed_n <= -2 ** 31:
            return 0

        if is_negative:
            return -reversed_n

        return reversed_n
