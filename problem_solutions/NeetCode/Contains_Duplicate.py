class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found = set()
        for n in nums:
            # if true, n is a duplicate
            if n in found:
                return True
            # otherwise, add to found
            else:
                found.add(n)
        # if you've gone through entire list
        # then there are no duplicates, so return False
        return False
        
