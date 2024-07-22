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
      
        res = defaultdict(list) #mapping the count of each char to the list of Anagrams 
                            # default dict(list) makes it default a list in case the value doesn't exist yet

        for i in strs:
            count = [0] * 26 #26 0's we add count of char to one of the zeros from a - z if found

            for c in i:
                count[ord(c) - ord("a")] # current number subtracted by 'a' maps it to the correct index above 
                                         # visual rep - a = 80 b = 81 in 'unicode' b = 81 - 'a' == 80 which will map to index '1'
                                         # += 1 increment it by 1
                                         
            res[tuple(count)].append(i) #list can not be keys in python so we make it tuple because it's immuatable (can't be changed)

        return res.values()
        