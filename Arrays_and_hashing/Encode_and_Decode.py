# Description
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Only $39.9 for the "Twitter Comment System Project Practice" within a limited time of 7 days!

# WeChat Notes Twitter for more information（WeChat ID jiuzhang104）


# Example
# Example1

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"
# Example2

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"


class Solution:
    def encode(self, strs):
        res = ""

        # Loop through each string in the input list 'strs'
        for s in strs:

            # Concatenate the length of the string as a string, followed by '#' and the string itself
            res += str(len(s)) + "#" + s
        
        # Return the encoded result as a single string
        return res

    def decode(self, s):
        # Initialize an empty list to store the decoded strings
        res = []

        # Initialize a pointer 'i' to keep track of the current position in the string 's'
        i = 0

        while i < len(s):
            # Initialize another pointer 'j' to find the position of the '#' character
            j = i

            # Iterate through 's' until '#' is encountered
            while str[j] != "#":
                j += 1

            # Extract the length of the next string by converting the substring from 'i' to 'j' to an integer
            length = int(s[i : j])

            # Append the substring following '#' (the actual string) to the 'res' list
            res.append(s[j + 1 : j + 1 + length])

            # Update the pointer 'i' to point to the next position after the decoded string
            i = j + 1 + length

        # Return the list of decoded strings
        return res
