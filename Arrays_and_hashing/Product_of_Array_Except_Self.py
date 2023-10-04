# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        #This creates an empty list for each "bucket" for ex: [][][][][][][] if nums is 6 
        freq = [[] for i in range(len(nums) + 1)]

        #uses the number puts in place of n if the number is not there it'll put it to 1 if so it'll increase it by 1
        for n in nums: 
            count[n] = 1 + count.get(n, 0)
        #iterates through the indexs and values where n is the number and c is the count of that number 
        for n, c in count.items(): 
        #This appends the number to the apprioate freq COUNT index that we made above 
            freq[c].append(n)

        res = []
        #this is where we return the result
        #it starts at top index then decrements by one 
        #It will find the highest count of each number and add it to the res list
        #it'll do this until the length of res  list is equal to k 
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n) 
                if len(res) == k:
                    return res
