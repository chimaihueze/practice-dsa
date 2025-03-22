"""Given an integer array nums, return true if any value appears more than once in the array, otherwise return false."""

def has_duplicate(list_of_numbers):
    new_set = set(list_of_numbers)

    if len(new_set) != len(list_of_numbers): return True
    return False

nums = [1, 2, 3, 3]
print(has_duplicate(nums))

nums2 = [1, 2, 3, 4]
print(has_duplicate(nums2))