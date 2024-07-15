# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #This is create the number of indexs needed for our output(same as length as input list) all indexs being 1's
        res = [1] * (len(nums))
        
        #Default the prefix to 1 so that if there is not prefix it stays the same
        prefix = 1
        #This gives a list of all the numbers before the value 
        #iterates through all of nums before final index 
        for i in range (len(nums)):
            #sets res list to prefix products which we use later 
            res[i] = prefix 
            prefix *= nums[i]
        #Default the postfix to 1 so that if there is not postfix it stays the same
        postfix = 1
        #Start at index one less than the length of list then stop when it greater than or equal to -1 and decrement by 1
        for i in range(len(nums) -1, -1, -1):
            #then we are going to do the same process backwards and once the loop is done we have our final answer
            res[i] *= postfix
            postfix *= nums[i]
        return res
