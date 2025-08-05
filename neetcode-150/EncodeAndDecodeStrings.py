from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""

        for word in strs:
            result+=str(len(word))
            result+=','        
        result += '%'
        for word in strs:
            result+=word
        print(result)
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        lengths = []
        separator_pos = 0
        num = ''
        for c in s:
            separator_pos += 1
            if c == ',':
                if len(num) > 0:
                    lengths.append(int(num))
                    num = ''
                continue
            if c == '%':
                break
            num = num + c
            print(num)
        print(lengths)
        for l in lengths:       
            print('length', l)     
            result.append(str(s[separator_pos:separator_pos+l]))
            separator_pos += l
        print(result)
        return result

if __name__ == '__main__':
    sol = Solution()
    sol.decode(sol.encode(["we","say",":","yes","!@#$%^&*()"]))
    