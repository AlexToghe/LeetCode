class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # left pointer, tells us where our unique value is placed next
        for i in range(len(nums)):  # right pointer that iterates through nums
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k










