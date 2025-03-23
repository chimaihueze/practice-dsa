"""
Given an array of integers nums and an integer target, 
return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
"""

def two_sum(nums, target):
    
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index if seen[complement] != index else None]
        
        seen[num] = index
    return []


nums = [1,4,5,6]
target = 10

print(two_sum(nums, target))

nums = [3,4,5,6]
target = 7

print(two_sum(nums, target))

nums = [5,5]
target = 10

print(two_sum(nums, target))