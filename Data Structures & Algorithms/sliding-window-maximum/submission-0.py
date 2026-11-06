from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # stores indices
        res = []

        for r in range(len(nums)):
            # 1. Pop smaller elements from the back to maintain decreasing order
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # 2. Add current index to deque
            q.append(r)

            # 3. Remove indices that are out of the active window [r - k + 1, r]
            if q[0] < r - k + 1:
                q.popleft()

            # 4. Once we have scanned at least k elements, record the window max
            if r >= k - 1:
                res.append(nums[q[0]])

        return res