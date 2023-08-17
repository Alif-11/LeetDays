class Solution:
    # I could not create a solution for this problem myself
    # This is a solution by user sudesh_pawar that I have committed to 
understanding
    # The post and pre variables act like giant garbage balls (hear me 
out)
    # They pick up copies of the numbers before and after nums[i]
    # post will multiply sol[i] with the product of the numbers before 
nums[i]
    # When post gets to nums[i], it will then multiply sol[i] (the product 
of the numbers before nums[i]) with the product of the numbers after 
nums[i]
    # Thus, each entry of sol[i] will contain the product of every element 
in nums except nums[i] itself.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)

        # parse through
        # nums = [1, 2, 3, 4]

        # before for loop
        # pre = 1, post = 1, sol = [1, 1, 1, 1]

        # * End of i=0 loop
        # pre = 1, post = 4, sol = [1, 1, 1, 1]

        # End of i=1 loop
        # pre = 2, post = 12, sol = [1, 1, 1 * 4, 1]

        # End of i=2 loop
        # pre = 6, post = 24, sol = [1, 1 * 3 * 4, 1 * 2 * 4, 1]

        # END of i=3 loop 
        # pre = 24, post = 24, sol = [2 * 3 * 4, 1 * 3 * 4, 1 * 2 * 4, 1 * 
2 *3]
