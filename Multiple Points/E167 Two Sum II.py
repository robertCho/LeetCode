from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return 0

    def twoSum_correct(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]

if __name__=="__main__":
    numbers = [2,3,4] 
    target = 6
    solution = Solution()    
    list_ind = solution.twoSum(numbers, target)
    print(list_ind)
