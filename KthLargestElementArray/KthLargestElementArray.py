"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in sorted order, not the kth distinct element.
Can you solve it without sorting?

input nums: [3,2,1,5,6,4]

"""
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        heap = [-x for x in nums]
        heapq.heapify(heap)

        for i in range(k):
            kth_largest = heapq.heappop(heap) * -1

        return kth_largest
        