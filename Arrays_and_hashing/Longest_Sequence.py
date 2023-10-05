class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #This creates our set 
        num_set = set(nums)
        #This is used to track longest sequence
        max_length = 0

        #This loop checks for the start of a new sequence
        for num in num_set:
            if num - 1 not in num_set:  
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:  # Check for consecutive numbers
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)  # Update the longest sequence

        return max_length