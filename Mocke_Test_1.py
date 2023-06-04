# Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# a. 1 <= nums.length <= 10^4
# b. -2^31 <= nums[i] <= 2^31 - 1

# -------------------------ANS-----------------
------------------------#

def moveZeroes(nums):
     """
    Function to move all zeroes to the end of the array while maintaining
    the relative order of the non-zero elements.
    """
    new_nums = [num for num in nums if num != 0] + [0] * nums.count(0)

    return new_nums
 
print(moveZeroes([0,1,0,3,12]))


# First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# Constraints:
# a. 1 <= s.length <= 10^5
# b. s consists of only lowercase English letters.

# -------------------------ANS-----------------------------------------#


def firstUniqChar(s):
    """
    Function to find the first non-repeating character in a string
    and return its index.
    """
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1
  
print(firstUniqChar('loveleetcode'))






