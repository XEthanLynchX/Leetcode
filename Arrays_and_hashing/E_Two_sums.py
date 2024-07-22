# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

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

        #basically we scan the whole array starting from index 0 the check the dif between the target and current number 
        #when the difference and current number are added we get our target
        #if the difference has already been stored in the array we return both the current number and the difference