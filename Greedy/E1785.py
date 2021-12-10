from typing import List
import math

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return 0
    def minElements_correct(self, nums: List[int], limit: int, goal: int) -> int:
        return math.ceil(abs(goal - sum(nums)) / limit)

if __name__=="__main__":

    Solution = Solution()
    output = Solution.minElements_correct([1,-1,1], limit = 3, goal = -4)
    print(output)