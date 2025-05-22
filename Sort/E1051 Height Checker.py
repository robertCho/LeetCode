from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height_sorted = sorted(heights)
        return len([ind for ind, _ in enumerate(heights) if heights[ind]!=height_sorted[ind]])

    def aheightChecker_correct(self, nums: List[int]) -> int:
        return 0


if __name__=="__main__":
    heights = [1,1,4,2,1,3] 
    solution = Solution()    
    ind = solution.heightChecker(heights)
    print(ind)