# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # Initialize an empty list to store the result (lists of unique triplets).
        nums.sort  # This is a typo, it should be 'nums.sort()' to sort the input list.

        for i, a in enumerate(nums):  # Loop through the sorted list using its index and value.
            if i > 0 and a == nums[i-1]:  # Check if the current value is the same as the previous one.
                continue  # If it is, skip to the next iteration to avoid duplicates.

            l, r = i + 1, len(nums) - 1  # Initialize left and right pointers for two-sum check.
            while l < r:  # While the left pointer is less than the right pointer.
                threeSum = a + nums[l] + nums[r]  # Calculate the sum of the three values.

                if threeSum > 0:
                    r -= 1  # If the sum is positive, decrement the right pointer.
                elif threeSum < 0:
                    l += 1  # If the sum is negative, increment the left pointer.
                else:
                    res.append([a, nums[l], nums[r]])  # If the sum is zero, add the triplet to the result list.
                    l += 1  # Move the left pointer to the right.
                    while nums[l] == nums[l-1] and l < r:
                        l += 1  # Skip duplicate values to avoid duplicate triplets.

        return res  # Return the list of unique triplets that sum to zero.


                    