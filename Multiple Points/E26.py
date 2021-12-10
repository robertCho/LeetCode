from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return not nums

    def removeDuplicates_buildin(self, nums: List[int]) -> int:
        print(id(nums))
        ans_nums = ['_']*len(nums)
        list_nums_sort = sorted(list(set(nums)))
        ans = len(list_nums_sort)
        ans_nums[:len(list_nums_sort)] = list_nums_sort
        nums[:] = ans_nums
        print(id(nums))
        return(ans, ans_nums)

    def removeDuplicates_correct(self, nums: List[int]) -> int:
        #Something wring
        i = 1
        for j in range(1, len(nums)):
            if nums[j - 1] < nums[j]:
                nums[i] = nums[j]
                i += 1
        return i, nums

if __name__=="__main__":

    Solution = Solution()
    inputs = [1,1,2]
    print(id(inputs))
    output, nums = Solution.removeDuplicates_buildin(inputs)
    
    print(output)
    print(nums)