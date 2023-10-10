# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        #left pointer starts at the index of 0
        l = 0
        #right pointer starts at the end of the string
        r = len(s) -1

        #while left is less than right(havent crossed over each other)
        while l < r:
           
           #skips over non alphanum character 
           #but also doesnt cross each pointer over eachother
            while l < r and not self.alphaNum(s[l]):
                l+= 1

           #skips over non alphanum character 
           #but also doesnt cross each pointer over eachother
            while r > l and not self.alphaNum(s[r]):
                r-= 1

            #if they dont match returns false ending the loop
            if s[l].lower() != s[r].lower():
                return False
            #increments left pointer up and right down
            l = l + 1
            r = r - 1
        return True

    def alphaNum(self, c):
            #using ASC value of character
            #we use ord to get ASC value of character
            #check if c(character we are checking) is a uppercase character
        return  (ord('A') <= ord (c) <= ord('Z') or
                ord('a') <= ord (c) <= ord('z') or
                ord('0') <= ord (c) <= ord('9'))