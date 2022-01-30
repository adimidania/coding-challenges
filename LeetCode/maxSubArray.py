'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
'''

# The idea here is to provide two sums, current sum and max sum as shown in the algorithm below.
# Every time the current sum is negative, we re-initialize it to zero, because there's absolutely no point
# to keep it since we are looking for the largest sum, maxsub will always store the largest sum current sum has
# found, sooo at the end of the process we will be getting the largest sum.
# Do an example with some prints and everything will get clear.
def maxSubArray(nums):
    maxSub = nums[0]
    cur_sum = 0
    for num in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += num
        maxSub = max(maxSub, cur_sum)
    return maxSub
