class Solution:
    """
    An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for ch_s , ch_t in zip(s,t):
            count[ord(ch_s) - ord('a')] += 1
            count[ord(ch_t) - ord('a')] -=1
        
        for c in count:
            if c != 0 :
                return False
        return True
    
if __name__ == "__main__":
    # Example usage
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))  # Output: True
    print(solution.isAnagram("rat", "car"))          # Output: False
