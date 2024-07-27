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
        #intialize Hashmap to store count
        count = {}
        #create a bucketsort that starts with an empty array and that is the size of our nums array and then increment by one 
        #It Creates empty array [][][][] if our list was 4 long for example
        freq = [[] for i in range(len(nums)+ 1)]
        
        #Loop the number through the all the nums list and increment the count of every number found 
        #This loops through starting it at 0 and increments by one if found adding it to our "count"
        for n in nums:
            #Then set count equal to the starting value of what our count begins at and increase by 1
            count[n] = count.get(n, 0) + 1
        #Loop the key value pairs n for number c for count in count  
        for n, c in count.items():
            #in freq array append the value of the number to the freq index of the count
            #where n is the number and c is the count
            freq[c].append(n)
        
        #intialize the res list
        res = []
        #loop through the freq array backards starting from the highest count
        #first value is the start second value is where you end last value is how increment / decrement
        for i in range(len(freq) - 1, 0, -1):
            #loop through every number in the freq list of i
            #where n is the number 
            for n in freq[i]:
                #append the number to the result
                res.append(n)
                #set a condition that if the length of our result is == to k return the result
                if len(res) == k:
                    return res        
             

        