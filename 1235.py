from typing import List

class Solution:

    dp = None

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        size = len(startTime)
        jobs = [[0] * 3 for _ in range(size)]

        self.dp = [-1] * size

        for index in range(size):
            jobs[index][0] = startTime[index]
            jobs[index][1] = endTime[index]
            jobs[index][2] = profit[index]

        jobs.sort(key=lambda row: row[0])

        return self.recursive(jobs, 0)

    def recursive(self, jobs: List[List[int]], index: int) -> int:
        if index == len(jobs):
            return 0
        if self.dp[index] != -1:  # Fix: use self.dp instead of dp
            return self.dp[index]
        nextPossibleIndex = self.next_index_bs(jobs, index)
        if nextPossibleIndex == -1:
            nextRecursiveProfit = 0
        else:
            nextRecursiveProfit = self.recursive(jobs, nextPossibleIndex)
        include = jobs[index][2] + nextRecursiveProfit
        exclude = self.recursive(jobs, index + 1)
        self.dp[index] = max(include, exclude)  # Fix: use self.dp instead of dp
        return self.dp[index]

    def next_index(self, jobs, index):
        next_index = index + 1
        while next_index < len(jobs):
            if jobs[index][1] <= jobs[next_index][0]:
                return next_index
            next_index += 1
        return -1

    def next_index_bs(self, jobs, index):
        found = -1
        low = index + 1
        high = len(jobs) - 1
        while low <= high:
            mid = low + (high - low) // 2
            # print(mid)
            if jobs[index][1] <= jobs[mid][0]:
                high = mid - 1
                found = 1
            else:
                low = mid + 1
        if found == -1:
            return -1 
        return low
