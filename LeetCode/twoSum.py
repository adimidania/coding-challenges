'''
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target. You may assume that each input would have exactly 
one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
# The most straightforward solution that came to my mind is the following
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i] + nums[j] == target):
                return[i,j]

# I looked up for other solutions and just found this one!
# Definitely MUCH MUCH MUCH faster than mine.
def twoSum(nums,target):
    key = {}
    #Loop through nums
    for i in range(0, len(nums)):
        #Checks if the current nums[i] is a second value to
        #Another nums[?] to make a successful pair
        if nums[i] in key.keys():
                
            return [key[nums[i]],i]
          
        #Uses current nums[i] and constant target to determine the
        #Second value necessary to make a successful pair
        key[target - nums[i]] = i