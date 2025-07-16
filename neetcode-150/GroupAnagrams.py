"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        str_dict = {}
        for str in strs:
            num_repr = self.to_int_array(str)
            if num_repr in str_dict:
                str_dict[num_repr].append(str)
            else:
                str_dict[num_repr] = [str]
        return list(str_dict.values())
    
    def to_int_array(self, str1:str):
        counter = [0] * 26
        for ch1 in str1:
            counter[ord(ch1) - ord('a')] +=1
        return tuple(counter)


if __name__ == "__main__":
    strs = ["act","pots","tops","cat","stop","hat"]
    # expected Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    solution = Solution()
    print (solution.groupAnagrams(strs))