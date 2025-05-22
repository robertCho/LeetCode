from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage: dict = {}
        for i, item in enumerate(nums):
            missing_num = target-item
            if storage.get(missing_num) is not None:
                return [i, storage.get(missing_num)]
            storage[item] = i
            
            


