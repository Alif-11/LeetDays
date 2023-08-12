class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Date: 8/12/2023
        Time: 16:04
        Purpose: Merge sorted arrays
        Runtime: 44 ms, beats 83.3% (Much better than the beats 10% I got with the other problems)
        Memory: 16.39 mb, beats 56.31% (Same thing with runtime, much better than before)
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0 # pointer for nums1
        j = 0 # pointer for nums2
        loc_last_n1 = m - 1
        while True:
            if j == n: # nothing else to insert
                return nums1
            if i > loc_last_n1: # put the rest of nums2 in nums1
                nums1[m+j : m+n] = nums2[j : n]
                return nums1
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                loc_last_n1 += 1
                i += 2
                j += 1
            else: # nums[1] must be > nums2[j]
                nums1.insert(i, nums2[j])
                nums1.pop()
                loc_last_n1 += 1
                i += 1
                j += 1
