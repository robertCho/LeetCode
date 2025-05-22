from typing import List
import itertools
import operator


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # ind_cut = []
        # list_devid = nums[1:] - nums
        # for ind, devid in enumerate(list_devid):
        #     if devid != 1: ind_cut.append(ind)
        # return [for ]
        groups = itertools.groupby(enumerate(nums),
                                   key=lambda enum: enum[1] - enum[0])
        ans = []
        for _, snippet in groups:
            snippet = list(map(operator.itemgetter(1), snippet))
            if snippet[0] == snippet[-1]:
                ans.append(str(snippet[0]))
            else:
                ans.append(f'{snippet[0]}->{snippet[-1]}')
        return ans