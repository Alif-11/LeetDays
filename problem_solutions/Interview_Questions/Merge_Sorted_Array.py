class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> 
None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0 # pointer for nums1
        j = 0 # pointer for nums2
        loc_last_n1 = m - 1
        while True:
            print(nums1)
            print(i)
            print(j)
            if j == n: # nothing else to insert
                print("a")
                return nums1
            if i > loc_last_n1: # put the rest of nums2 in nums1
                print("b")
                nums1[m+j : m+n] = nums2[j : n]
                return nums1
            if nums1[i] < nums2[j]:
                print("c")
                i += 1
            elif nums1[i] == nums2[j]:
                print("d")
                nums1.insert(i, nums2[j])
                nums1.pop()
                loc_last_n1 += 1
                i += 2
                j += 1
            else: # nums[1] must be > nums2[j]
                print("e")
                nums1.insert(i, nums2[j])
                nums1.pop()
                loc_last_n1 += 1
                i += 1
                j += 1
            print(nums1)
            print(i)
            print(j)
        print("f")
