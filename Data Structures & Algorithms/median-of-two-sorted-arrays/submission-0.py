class Solution:

  def findMedianSortedArrays(
      self, nums1: list[int], nums2: list[int]
  ) -> float:
    # Ensure binary search runs on the smaller array: O(log(min(m, n)))
    A, B = nums1, nums2
    if len(A) > len(B):
      A, B = B, A

    m, n = len(A), len(B)
    total = m + n
    half = (total + 1) // 2

    left, right = 0, m

    while left <= right:
      i = (left + right) // 2  # Partition in A
      j = half - i  # Partition in B

      # Boundary values (use +/- infinity for empty partitions)
      A_left = A[i - 1] if i > 0 else float("-inf")
      A_right = A[i] if i < m else float("inf")
      B_left = B[j - 1] if j > 0 else float("-inf")
      B_right = B[j] if j < n else float("inf")

      # Check if partition is valid
      if A_left <= B_right and B_left <= A_right:
        if total % 2 != 0:
          return float(max(A_left, B_left))
        return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
      elif A_left > B_right:
        right = i - 1  # Too many elements taken from A
      else:
        left = i + 1  # Too few elements taken from A

    return 0.0