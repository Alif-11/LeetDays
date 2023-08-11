class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """ 
            Date: 8/10/2023
            Time: 11:18
            Purpose: Find the kth factor of n (k=1 would be 1), or return -1 if the kth factor of n doesn't exist.
            
            We will start off with a simple solution
            We will create a dictionary of factors:
            - keys will be integers
            - values will be the factors of 'n'
            * We will then use the '[dictionary].get(key=k, default=-1)' 
method
            * to return the factor corresponding to k.
            If the provided k is not in our dictionary, return -1 

            Code checkpoints: 
            - factors_list: a list that contains all distinct factors of n 
in
                            ascending order
        """
        factors_list = []
        index = 0
        # * x3 we will set a modifiable end for the range that will be set 
to
        # * the larger of every factor pair
        # Fix x3 resolves issues with x1

        # x6 changed ender to deal with cases where n=1
        ender = n+1
        # * x1 we will see every possible factor and their pair by 
(n+1)//2
        # * for i in range(1, (n//2) ):
        
        # X for i in (1, ender):
        # * x7 changed the above commented for loop to a while loop
        # * to provide a way to terminate the range of values i loops
        # * over early

        # x8 forgot to initialize i and iterate by 1 in loop
        i = 1
        while i < ender:
            # if i divides evenly into n
            if n%i == 0:
                factors_list.insert(index, i)
                # x4 avoiding duplicate factors in factors_list
                # x5 changed i to n//i in the below for loop
                if n//i not in factors_list:
                    factors_list.insert(index+1, n//i)
                # x2 iterate index by 1
                index += 1
                ender = n//i
            i += 1
            print("list", factors_list)
            print("ender", ender)
            print("i", i)
        # checkpoint: factors_list works after fix x3
        """factors_dict = dict()
        for index, factor in enumerate(factors_list):
            factors_dict[index+1] = factor
        # checkpoint: factors_dict works after above for loop
        return factors_dict.get(k, -1)"""
        # o1 we dont actually need factors_dict. the following code does 
fine
        if factors_list[k-1:k] == []:
            return -1
        return factors_list[k-1:k][0]
