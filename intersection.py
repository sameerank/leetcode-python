class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
import unittest

sol = Solution()

class TestIntersection(unittest.TestCase):

    def test_no_intersection(self):
        self.assertEqual(sol.intersection([1, 2], [3, 4]), [])

    def test_one_intersection(self):
        self.assertEqual(sol.intersection([1, 2], [2, 3]), [2])

    def test_two_intersection(self):
        self.assertEqual(sol.intersection([1, 2, 3], [2, 3, 4]), [2, 3])

    def test_three_intersection(self):
        self.assertEqual(sol.intersection([1, 2, 3, 4], [2, 3, 4, 5]), [2, 3, 4])

if __name__ == '__main__':
    unittest.main()
