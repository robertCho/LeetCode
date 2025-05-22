from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        return 0
    def specialArray_correct(self, nums: List[int]) -> int:
        return 0


if __name__=="__main__":
    heights = [1,1,4,2,1,3] 
    solution = Solution()    
    ind = solution.heightChecker(heights)
    print(ind)