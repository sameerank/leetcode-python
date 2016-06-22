class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        intersection = []
        idx1, idx2 = 0, 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                intersection.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return intersection
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
import unittest

sol = Solution()

class TestIntersect(unittest.TestCase):

    def test_example(self):
        self.assertEqual(sol.intersect([1, 2, 2, 1], [2, 2]), [2, 2])

if __name__ == '__main__':
    unittest.main()
