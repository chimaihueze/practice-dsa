"""Given an integer array nums, return true if any value appears more than once in the array, otherwise return false."""

nums = [1, 2, 3, 3]

nums2 = [1, 2, 3, 4]


def has_duplicate(list_of_numbers):
    new_list = []

    for num in list_of_numbers:
        if num in new_list:
            return True
        else:
            new_list.append(num)
    return False

print(has_duplicate(nums))
print(has_duplicate(nums2))