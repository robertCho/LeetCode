from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind =0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ind] = nums[i]
                ind += 1
        return ind 

    def removeElement_correct(self, nums: List[int], val: int) -> int:
        i, last = 0, len(nums)
        while i < last:
            if nums[i] == val:
                last -= 1
                nums[i] = nums[last]
            else:
                i += 1
        return last

if __name__=="__main__":

    Solution = Solution()
    # nums = [0,1,2,2,3,0,4,2], val = 2
    # nums = [3,2,2,3], val = 3
    inputs= [0,1,2,2,3,0,4,2]
    val = 2
    num = Solution.removeElement_correct(inputs, val)
    print(inputs[:num])
