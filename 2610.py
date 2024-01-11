from typing import List


# Input: nums = [1,3,4,1,2,3,1]
# Output: [[1,3,4,2],[1,3],[1]]
# Explanation: We can create a 2D array that contains the following rows:
# - 1,3,4,2
# - 1,3
# - 1
# All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
# It can be shown that we cannot have less than 3 rows in a valid array.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: [[4,3,2,1]]
# Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return [[]]
        map = [0] * 201
        



Solution().findMatrix([])