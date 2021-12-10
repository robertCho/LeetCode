from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n, ans = len(strs), len(strs[0]), 0
        for j in range(n):
            for i in range(1, m):
                if strs[i][j] < strs[i-1][j]:
                    ans += 1
                    break
        return ans

    def minDeletionSize_correct(self, strs: List[str]) -> int:
        m, n, ans = len(strs), len(strs[0]), 0
        for j in range(n):
            for i in range(1, m):
                if strs[i][j] < strs[i-1][j]:
                    ans += 1
                    break
        return ans

if __name__ == "__main__":
    Solution = Solution()
    input = ["caf","dba","gcb"]
    output = Solution.minDeletionSize(input)
    print(output)