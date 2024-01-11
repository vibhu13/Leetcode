from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int :
        ans = 0
        prev = 0
        for row in bank:
            count = 0
            size = len(row)

            for i in range(size):
                if row[i] == '1':
                    count +=1

            if count > 0:
                    ans += prev*count
                    prev = count
        # print(ans)
        return ans

Solution().numberOfBeams(["011001","000000","010100","001000"])