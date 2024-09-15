"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in sorted order, not the kth distinct element.
Can you solve it without sorting?

input nums: [3,2,1,5,6,4]
"""
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        Since a heap keeps track of items in decreasing order, we want to negate nums.
        The largest element will be the smallest element (first element in heap).
        """
        heap = [-x for x in nums]  # creating array of negated elements from nums
        heapq.heapify(heap)  # reordering in terms of increasing order

        # we now pop k times and multiply value by -1 to extract the kth largest element
        for i in range(k):
            kth_largest = heapq.heappop(heap) * -1

        return kth_largest
