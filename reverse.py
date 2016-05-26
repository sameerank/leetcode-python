class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_stringified = str(x)
        if x_stringified[0] == '-':
            return int('-' + x_stringified[1::][::-1])
        else:
            return int(x_stringified[0::][::-1])
