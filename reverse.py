class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_stringified = str(x)
        if x_stringified[0] == '-':
            res = int('-' + x_stringified[1::][::-1])
        else:
            res = int(x_stringified[::-1])
        return 0 if abs(res) > 2147483650 else res
