
'''
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''
# Pretty intuitive solution is to sort the array, if nums[j] is equal to nums[j+1] then we have a duplicate
def containsDuplicate(nums):
    nums.sort()
    j = 0
    while(j<len(nums)-1):
        if(nums[j] == nums[j+1]):
            return True
        else:
            j = j + 1
    return False

# I looked up for other people's solutions
# Here's what I found!

# Using set
def containsDuplicateSet(nums):
    if len(nums)==len(set(nums)) :
        return False
    else:
        return True

# Using dict
def containsDuplicateDict(nums): 
    d = {}
    for i in nums:
        if i in d:
            return True
        else:
            d[i] = 1
    return False
