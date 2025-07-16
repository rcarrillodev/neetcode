from typing import List

class Solution:
    """
        Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
        You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
        Return the answer with the smaller index first.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in remaining:
                return [remaining[num],i]
            res = target - num
            remaining[res] = i
            print(remaining)
        return []

if __name__ == "__main__":
    # Scenario 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test 1:", Solution().twoSum(nums1, target1))  # Expected output: [0, 1]

    # Scenario 2
    nums2 = [3, 2, 4]
    target2 = 6
    print("Test 2:", Solution().twoSum(nums2, target2))  # Expected output: [1, 2]