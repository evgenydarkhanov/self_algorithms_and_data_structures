"""
Input: nums = [1, 2, 3, 1]
dp = [1, 2, 4, 4]
Output: 4

Input: nums = [2, 7, 9, 3, 1]
dp = [2, 7, 11, 11, 12]
Output: 12
"""

from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
        return max(nums)

    dp = [0 for _ in range(n)]

    dp[0] = nums[0]
    dp[1] = max(dp[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[-1]


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4, f"{rob([1, 2, 3, 1]) = }"
    assert rob([2, 7, 9, 3, 1]) == 12, f"{rob([2, 7, 9, 3, 1]) = }"
    assert rob([9, 17, 9]) == 18, f"{rob([9, 17, 9]) = }"
    assert rob([9, 10]) == 10, f"{rob([9, 10]) = }"
    assert rob([1]) == 1, f"{rob([1]) = }"
