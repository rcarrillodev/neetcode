from typing import List
class Solution:
    """
    Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
    Each product is guaranteed to fit in a 32-bit integer. 
    """

    def productExceptSelf(self, nums:List[int]) -> List[int]:
        output = [1]*len(nums)
        left_prod = 1
        for i in range(0, len(nums)):
            output[i] = left_prod
            left_prod*=nums[i]
        right_product = 1
        for i in range(len(nums) -1 , -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        return output


if __name__ == "__main__":
    sol = Solution()
    numbers = [1,2,4,6]
    res = sol.productsExceptSelf(numbers)
    print(res)
    assert res == [48,24,12,8]
