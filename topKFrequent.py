class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        freq = collections.Counter()
        for num in nums:
            freq[num] += 1
        return map(lambda x: x[0], freq.most_common(k))
