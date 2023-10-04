# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
        #create a hashmap to store the count of each letter in each string
        hashmap = defaultdict(list)

        #iterate through each string and store the count of each letter in the hashmap
        for i in strs: 
            count = [0] * 26 

        #ord() returns an integer representing the Unicode character
        #subtracting the unicode of "a" from the unicode of the current character gives the index of the current character in the count array
            for c in i:
                count[ord(c) - ord("a")] += 1 

            #convert the count array to a tuple and store the string in the hashmap
            hashmap[tuple(count)].append(i)
        #return the values of the hashmap
        return hashmap.values()