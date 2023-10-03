class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {} # val : index 

    #enumerate is a function that iterates through a sequence 
    #while keeping track of the index
        for i, n in enumerate(nums): 
            #we define what difference is
            # Calculate the difference needed to 
            #reach the 'target' from the current element 'n'.4
            difference = target - n

            if difference in prevMap:
            # 'prevMap[difference]' gives the index of the element with value 'difference',
            # and 'i' is the current index corresponding to 'n'.
                return [prevMap[difference], i]
            # If the 'difference' is not found in 
            #'prevMap', store the current element 'n' and its index 'i' in 'prevMap'.
             # This way, we keep track of elements we have seen so far.
            prevMap[n] = i
        # If the loop completes without finding a valid pair, return None.
        # This means that no two elements in the 'nums' list add up to the 'target'.