from typing import List

class TopKthFrequentElements:
    """
    Given an integer array nums and an integer k, return the k most frequent elements within the array.
    The test cases are generated such that the answer is always unique.
    You may return the output in any order.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = self.bucket_sort(nums, k)
        return result
    
    def bucket_sort(self, nums: List[int], k:int) -> List[int]:
        freq = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
            
        for num, count in freq.items():
            buckets[count].append(num)
        
        result = []
        for i in range(len(nums) , 0 , -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result

    

if __name__ == "__main__":
    numbers = [1,2]
    solution = TopKthFrequentElements()
    print (solution.topKFrequent(numbers, 2))
                    
