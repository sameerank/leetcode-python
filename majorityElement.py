class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]

import unittest

sol = Solution()

class TestMajorityElement(unittest.TestCase):

    def test_example(self):
        ary = ['a', 'b', 'c', 'b', 'c', 'c']
        self.assertEqual(sol.majorityElement(ary), 'c')

if __name__ == '__main__':
    unittest.main()
