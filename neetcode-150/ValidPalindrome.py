"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Constraints:

    1 <= s.length <= 1000
    s is made up of only printable ASCII characters.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum,s.replace(' ', '').lower())) #remove non-alphanumeric , then remove whitespaces, then make it lowercase
        print(s)
        if len(s) < 2 : 
            return True
        if len(s) == 2 :
            return self.areCharsEquals(s[0],s[1])
        i = 0
        j = len(s)-1
        mid = len(s)//2
        while i<=mid and j>=mid:
            if not self.areCharsEquals(s[i],s[j]):
                return False
            i+=1
            j-=1
        return True
    
    def areCharsEquals(self, a:str, b:str):
        if len(a) > 1 or len(b) > 1:
            raise ValueError('passed a string instead of char')
        return a == b
    

sol = Solution()
s = sol.isPalindrome("Was it a car or a cat I saw?")
print(s)
assert(s == True)
s = sol.isPalindrome("No lemon, no melon")
print(s)
assert(s == True)
s = sol.isPalindrome("a")
print(s)
assert(s == True)
s = sol.isPalindrome("ab")
print(s)
assert(s == False)
s = sol.isPalindrome("race a car")
print(s)
assert(s == False)