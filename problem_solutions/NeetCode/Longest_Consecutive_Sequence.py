class Solution:

    # Solution by a deleted user. Very elegant
    def longestConsecutive(self, nums: List[int]) -> int:
        # length of biggest sequence
        longest = 0
        # convert num_set into a set of nums
        num_set = set(nums)

        # for each number
        for n in num_set:
            # if n-1 is in the set, either you checked it or you will 
check it. there's no need to worry about running through your sequence now
            # if there is no n-1 in the set, it's go time
            if (n-1) not in num_set:
                # set your length to 1
                length = 1
                # as you keep finding consecutive numbers, keep increasing 
the length by 1
                while (n+length) in num_set:
                    length += 1
                # when finished going through the sequence, find the 
bigger value - your reigning longest value, or the current length.
                # set your longest variable to the bigger of those two
                longest = max(longest, length)
        # return the longest sequence
        return longest
