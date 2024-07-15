# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

      #if length of strings dont match, return false
        if len(s) != len(t):
            return False
      #create two dictionaries to store the count of each letter in each string
        countS = {}
        countT = {}

      #iterate through each string and store the count of each letter in the dictionary
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #compare the two dictionaries
        #if the count of any letter in the two dictionaries dont match, return false
        for i in countS:
            if countS[i] != countT.get(i):
                return False
        return True
        

