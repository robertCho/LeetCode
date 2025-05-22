class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # corner case
        if m == 1 and n == 1:
            return 1
        metrix = [[0] * n for _ in range(m)]
        metrix[0] = [1]*n
        for i in range(m):
            metrix[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                metrix[i][j] = metrix[i-1][j] + metrix[i][j-1]
        return metrix[-1][-1]

        