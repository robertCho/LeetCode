class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<2:
            return s
        left, right = 0, 0
        p = [[0]*n for _ in range(n)]
        for i in range(n):
            p[i][i] = True
        for j in range(1,n):
            for i in range(0,j):
                innerIsPalind = p[i+1][j-1] or j-i<2
                if(s[i]==s[j] and innerIsPalind):
                    p[i][j] = True
                    if (j-i > right -left):
                        left = i
                        right = j

        return s[left:right+1]