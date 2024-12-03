# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def reverse(self, x: int) -> int:
        int_num = 2**31

        if x < 0:
            a = -1 * int(str(x)[1:][::-1])
        else:
            a = int(str(x)[::-1])

        if a <= -int_num or a >= int_num-1:
            return 0
        else:
            return a