from typing import List


class Solution:
    def dominantIndex(self, nums:List[int]) -> int:
        idx, largest, second = -1, -1, -1
        for i, num in enumerate(nums):
            if num > largest:
                largest, second = num, largest
                idx = i
            elif num > second:
                second = num
        return idx if largest >= 2 * second else -1