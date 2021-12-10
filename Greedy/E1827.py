from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op_time = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                op_time += nums[i-1] - nums[i] +1
                nums[i] = nums[i-1] + 1
        return op_time
        
    def minOperations_correct(self, nums: List[int]) -> int:
        op_time = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                op_time += nums[i-1] - nums[i] +1
                nums[i] = nums[i-1] + 1
        return op_time



if __name__ == "__main__":

    Solution = Solution()
    inputs = [1,1,1]
    output = Solution.minOperations_correct(inputs)
    print(output)
    print('\n')