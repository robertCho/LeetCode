from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        return sum(nums_sort[::2])


    def arrayPairSum_correct(self, nums: List[int]) -> int:
        return 0


if __name__=="__main__":
    nums = [6,2,6,5,1,2] 
    solution = Solution()    
    max = solution.arrayPairSum(nums)
    print(max)