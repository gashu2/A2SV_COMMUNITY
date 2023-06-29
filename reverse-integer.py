class Solution:
    def reverse(self, x: int) -> int:
        int_str = str(x)
        reversed_int = 0
        if x < 0:
            new_int = -1 * x
            str_int = str(new_int)
            reversed_int = -1 * int(str_int[::-1])
        else:
            reversed_int = int(int_str[::-1])
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            reversed_int = 0
        return reversed_int
