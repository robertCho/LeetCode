from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(ch for ch in s if ch.isalnum()).lower()
        s2 = s1[::-1]
        return s1 == s2

    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(ch for ch in s if ch.isalnum()).lower()
        s2 = s1[::-1]
        return s1 == s2

    def isPalindrome_correct(self, s: str) -> bool:
        return 0

if __name__=="__main__":

    Solution = Solution()
    s = "A man, a plan, a canal: Panama"
    
    is_palimdrome = Solution.isPalindrome(s)
    print(is_palimdrome)
