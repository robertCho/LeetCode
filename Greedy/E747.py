from typing import List
class Solution:
    def dominantIndex(self, nums:List[int]) -> int:
        if len(nums) == 1: return 0

        max, second = -1, -1
        for ind, i in enumerate(nums):
            a = 10

    def dominantIndex_correct(self, nums:List[int]) -> int:
        idx, largest, second = -1, -1, -1
        for i, num in enumerate(nums):
            if num > largest:
                largest, second = num, largest
                idx = i
            elif num > second:
                second = num
        return idx if largest >= 2 * second else -1
        
if __name__=="__main__":

    Solution = Solution()
    nums = [1]
    output = Solution.dominantIndex_correct(nums)
    print(output)