from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        return 0

    def merge_correct(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        return 0

if __name__=="__main__":

    Solution = Solution()
    nums1 = [1,2,3,0,0,0] 
    m, n = 3, 3
    nums2 = [2,5,6] 
    num = Solution.merge(nums1, m, nums2, n)
    print(nums1[:num])
