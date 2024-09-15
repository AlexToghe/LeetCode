"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
 of all the values of the nodes in the tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

""""
The logic behind this problem. To perform a BFS traversal and append all nodes to a queue. Then add all nodes to a heap.
After that, pop out k terms to extract the kth smallest element.
"""
from collections import deque
import heapq
class Solution(object):
    def kthSmallest(self, root, k):
        q = deque([root])
        heap = []

        while q:
            node = q.popleft()
            heap.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        heapq.heapify(heap)
        for i in range(0, k):
            kth_smallest = heapq.heappop(heap)

        return kth_smallest