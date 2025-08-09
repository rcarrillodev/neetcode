'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
'''
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pool = set(nums)
        longest = 0
        for num in nums:
            t = num - 1
            if t not in pool:
                count = 1
                while num + count in pool:
                    count+=1
                if count > longest:
                    longest = count
        return longest


sol = Solution()
nums = [2,20,4,10,3,4,5]
result = sol.longestConsecutive(nums)
print(result)
assert result == 4
