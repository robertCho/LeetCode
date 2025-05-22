from Array.E228 import Solution
import operator
if __name__=="__main__":

    Solution = Solution()
    # nums = [3,6,1,0]
    # output = Solution.dominantIndex(nums)
    # print(output)

    # prices = [7,1,5,3,6,4]
    # sub = map(operator.sub, prices[1:], prices)
    # print(list(sub))
    # Solution = Solution()
    # out = Solution.maxProfit(prices)
    # print(out)


    nums = [0,1,2,4,5,7,13]
    output = Solution.summaryRanges(nums)
    print(output)
