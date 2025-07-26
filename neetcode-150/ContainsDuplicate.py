from typing import List

class Solution:
    """
    Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
    ToDo: This solution relies on manually sorting the list
    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False   
    

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    print(solution.hasDuplicate([1, 2, 3, 4]))  # Output: False
    print(solution.hasDuplicate([1, 2, 3, 1]))  # Output: True