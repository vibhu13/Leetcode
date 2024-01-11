from typing import List

class Solution:

  def findContentChildren(self, greed: List[int], size: List[int]) -> int:
    greed.sort()
    size.sort()
    maxNum = 0
    cookieIndex = len(size) - 1
    greedIndex = len(greed) - 1
    while cookieIndex >= 0 and greedIndex >= 0:
      if size[cookieIndex] >= greed[greedIndex]:
        maxNum += 1
        cookieIndex -= 1
        greedIndex -= 1
      else:
        greedIndex -= 1

    # for printing remove it 
    print(maxNum)
    return maxNum


Solution().findContentChildren([1, 2], [1, 2, 3])