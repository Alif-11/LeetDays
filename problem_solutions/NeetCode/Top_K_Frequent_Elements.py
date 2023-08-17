from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        # frequency is now a dictionary that 
        # maps elements in 'nums' to
        # their frequency in 'nums'
        for n in nums:
            frequency[n] = frequency[n] + 1
        
        freq_to_ele = defaultdict(list)
        # freq_to_ele is now a dictionary that
        # maps frequencies in 'nums'
        # to the elements in 'nums' with those frequencies
        for ele, freq in frequency.items():
            freq_to_ele[freq].append(ele)
        
        # get the highest frequencies
        highest_freqs = sorted(freq_to_ele.keys(), reverse=True)
        return_list = list()
        for freq in highest_freqs:
            # for each element in the list associated with
            # each frequency (which is a key value)
            for ele in freq_to_ele[freq]:
                # append the element to the return list
                return_list.append(ele)
                # if your return list has the appropriate length,
                # return it
                if len(return_list) == k:
                    return return_list

