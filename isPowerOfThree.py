class Solution(object):
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        elif n >= 3:
            n = n / 3.0
            return self.isPowerOfThree(n)
        else:
            return False
        """
        :type n: int
        :rtype: bool
        """
