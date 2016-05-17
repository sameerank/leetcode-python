class Solution(object):
    def isPowerOfFour(self, num):
        if num == 1:
            return True
        elif num >= 4:
            num = num / 4.0
            return self.isPowerOfFour(num)
        else:
            return False
        """
        :type num: int
        :rtype: bool
        """
