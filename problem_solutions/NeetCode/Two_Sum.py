class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this is a dict that maps the elements of nums
        # to their respective indices
        ele_to_ind = {}
        # iterate through nums
        for i in range(len(nums)):
            # if the complement (target-nums[i]) of the current element is 
in 
            # the dict, return the index ele_to_ind[target-nums[i]] 
            # associated with the complement
            # and the index (i) of the current element
            complement = target-nums[i]
            if complement in ele_to_ind:
                # there must be exactly one pair 
                # of indices for our solution so
                # we don't need more return statements
                return [ele_to_ind[complement], i]
            # keep up the element to index mapping
            # this will build a dictionary of potential complements
            # future elements of nums can learn from 
            ele_to_ind[nums[i]] = i
