'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.
'''
from typing import Counter


def intersect(nums1, nums2):
    # The counter is a dict, the keys are the elements of the array
    # While the values are how many times the element occured in the array
    c = Counter(nums1)
    out = []
    for i in nums2:
        if(c[i] > 0):
            out.append(i)
            c[i] = c[i] - 1
    return out


print(intersect([2,3,4,5,6,1,1,9], [1,1,4,5]))