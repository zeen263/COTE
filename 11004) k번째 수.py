import sys

N, k = map(int, sys.stdin.readline().split())
nums = map(int, sys.stdin.readline().split())

nums = sorted(nums)
print(nums[k-1])