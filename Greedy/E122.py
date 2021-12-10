from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans
    def maxProfit_correct(self, prices: List[int]) -> int:
        return(sum(cur-prev for prev, cur in zip(prices, prices[1:]) if cur > prev))

if __name__=="__main__":

    Solution = Solution()
    prices = [7,1,5,3,6,4]
    output = Solution.maxProfit_correct(prices)
    print(output)