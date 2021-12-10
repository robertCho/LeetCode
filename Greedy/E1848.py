from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        list_ind = []
        for ind, i in enumerate(nums):
            if i == target:
                list_ind.append(ind)
        min = abs(list_ind[0] - start)
        for j in range(1, len(list_ind)):
             if abs(list_ind[j] - start)<min:
                 min = abs(j - start)
        return min
    
    def getMinDistance_correct(self, nums: List[int], target: int, start: int) -> int:
        l = r = start
        while l >= 0 or r < len(nums):
            if l >= 0 and nums[l] == target: return start - l
            if r < len(nums) and nums[r] == target: return r - start
            l -= 1
            r += 1

if __name__ == "__main__":

    Solution = Solution()
    # inputs = ([1,2,3,4,5], target = 5, start = 3)
    output = Solution.getMinDistance_correct([1,2,3,4,5], target = 5, start = 3)
    print(output)
    print('\n')