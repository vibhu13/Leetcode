from typing import List 

class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        maxRange = 1000001
        size = len(nums)
        countList = [0] * maxRange
        for num in nums:
            countList[num] += 1
        index = 0
        
        while index < maxRange:
            ops5 = ops3 = ops2 = ops = maxRange
            value = countList[index]
            if value == 0:
                index += 1
                continue
            elif value % 5 == 0:
                ops5 = 2 * (value//5)
                # ans += 2 * (value//5)
                countList[index] = 0
                index += 1
            elif value % 3 == 0:
                ops3 = value//3
                # ans += value//3
                countList[index] = 0
                index += 1
            elif value % 2 == 0:
                ops2 = value//2
                # ans += value//2
                countList[index] = 0
                index += 1
            elif value == 1:
                ans = -1
                break
            else:
                value -= 3
                ops = 1
                # ans += 1
                countList[index] = value 
            ans += min(ops5,ops3,ops2,ops)
        return ans

print(Solution().minOperations([19,19,19,19,19,19,19,19,19,19,19,19,19]))
        



''' 
[2,3,3,2,2,4,2,3,4]

2:4
3:3
4:2

 '''