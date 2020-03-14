# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

nums = [2, 7, 11, 15]
target = 9
l = {}

def two_sum(nums, target):
    for x, y in enumerate(nums):
        if target - y in l:
            print(l[target - y], x)
        l[y] = x

two_sum(nums, target)