/*
 You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

 Merge nums1 and nums2 into a single array sorted in non-decreasing order.

 The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
 */
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int midx = m - 1; // index for nums1
        int nidx = n - 1; // index for nums2
        int right = m + n - 1; // index for nums 1
        while(nidx >= 0) {
            if (midx >= 0 and nums1[midx] > nums2[nidx]){
                nums1[right] = nums1[midx];
                midx --;
            }
            else{
                nums1[right] = nums2[nidx];
                nidx --;
            }
            right --;
        }
    }
};
